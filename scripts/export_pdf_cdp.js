#!/usr/bin/env node
/**
 * CDP-based PDF export — no default Chrome headers/footers,
 * PDF outline/bookmarks from headings.
 * Uses local HTTP server (not file://) for reliable headless navigation.
 * Usage: node export_pdf_cdp.js <html_path> <pdf_path> <book_title>
 */

const { spawn } = require('child_process');
const WebSocket = require('ws');
const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const HTML_PATH = process.argv[2];
const PDF_PATH = process.argv[3];
const BOOK_TITLE = process.argv[4] || 'AI for Everyone';

if (!HTML_PATH || !PDF_PATH) {
  console.error('Usage: node export_pdf_cdp.js <html_path> <pdf_path> [book_title]');
  process.exit(1);
}

const htmlAbs = path.resolve(HTML_PATH);
const pdfAbs = path.resolve(PDF_PATH);
const serveDir = path.dirname(htmlAbs);
const htmlName = path.basename(htmlAbs);
const HTTP_PORT = 18723;

function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

// ── Simple HTTP file server ──────────────────────────────────────────

function startServer(dir) {
  return new Promise((resolve, reject) => {
    const mimeMap = {
      '.html': 'text/html; charset=utf-8',
      '.css': 'text/css; charset=utf-8',
      '.js': 'application/javascript; charset=utf-8',
      '.svg': 'image/svg+xml',
      '.png': 'image/png',
      '.jpg': 'image/jpeg',
      '.woff2': 'font/woff2',
    };
    const server = http.createServer((req, res) => {
      const parsed = url.parse(req.url);
      let filePath = path.join(dir, decodeURIComponent(parsed.pathname));
      // Security: prevent directory traversal
      if (!filePath.startsWith(dir)) { res.statusCode = 403; res.end('Forbidden'); return; }
      if (fs.statSync(filePath, { throwIfNoEntry: false })?.isDirectory()) {
        filePath = path.join(filePath, 'index.html');
      }
      const ext = path.extname(filePath).toLowerCase();
      const contentType = mimeMap[ext] || 'application/octet-stream';
      try {
        const data = fs.readFileSync(filePath);
        res.writeHead(200, { 'Content-Type': contentType, 'Access-Control-Allow-Origin': '*' });
        res.end(data);
      } catch {
        res.statusCode = 404;
        res.end('Not Found');
      }
    });
    server.listen(HTTP_PORT, '127.0.0.1', () => resolve(server));
    server.on('error', reject);
  });
}

// ── Browser discovery ────────────────────────────────────────────────

async function findBrowser() {
  const candidates = process.platform === 'win32'
    ? [
        path.join(process.env['PROGRAMFILES'] || 'C:\\Program Files', 'Microsoft\\Edge\\Application\\msedge.exe'),
        path.join(process.env['PROGRAMFILES(X86)'] || 'C:\\Program Files (x86)', 'Microsoft\\Edge\\Application\\msedge.exe'),
        path.join(process.env.LOCALAPPDATA || '', 'Microsoft\\Edge\\Application\\msedge.exe'),
      ]
    : ['google-chrome', 'chrome', 'chromium', 'chromium-browser', 'msedge'];

  for (const c of candidates) {
    if (fs.existsSync(c)) return c;
  }
  throw new Error('No Chrome/Edge browser found');
}

// ── CDP helpers ──────────────────────────────────────────────────────

async function getWsUrl(port, retries = 20) {
  for (let i = 0; i < retries; i++) {
    try {
      const data = await new Promise((resolve, reject) => {
        http.get(`http://localhost:${port}/json`, res => {
          let body = '';
          res.on('data', chunk => body += chunk);
          res.on('end', () => resolve(body));
        }).on('error', reject);
      });
      const pages = JSON.parse(data);
      if (pages.length > 0) return pages[0].webSocketDebuggerUrl;
    } catch (e) { /* retry */ }
    await sleep(500);
  }
  throw new Error(`Could not connect to Chrome debug port ${port}`);
}

async function sendCommand(ws, method, params = {}) {
  const id = Math.floor(Math.random() * 1000000);
  return new Promise((resolve, reject) => {
    const handler = (data) => {
      const msg = JSON.parse(data.toString());
      if (msg.id === id) {
        ws.removeListener('message', handler);
        if (msg.error) reject(new Error(`${method}: ${JSON.stringify(msg.error)}`));
        else resolve(msg.result);
      }
    };
    ws.on('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

// ── Main ─────────────────────────────────────────────────────────────

async function main() {
  // 1. Start HTTP server
  console.log(`Starting HTTP server on port ${HTTP_PORT}...`);
  const httpServer = await startServer(serveDir);
  const pageUrl = `http://127.0.0.1:${HTTP_PORT}/${htmlName}`;
  console.log(`Serving: ${serveDir}`);

  // 2. Start browser
  const browser = await findBrowser();
  console.log(`Browser: ${browser}`);

  const cdpPort = 9224;
  const browserProc = spawn(browser, [
    `--remote-debugging-port=${cdpPort}`,
    '--headless',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--no-first-run',
    '--no-default-browser-check',
    'about:blank'
  ], { stdio: 'ignore', detached: false });

  let wsUrl;
  try {
    wsUrl = await getWsUrl(cdpPort, 25);
    console.log('CDP connected');
  } catch (e) {
    browserProc.kill();
    httpServer.close();
    throw e;
  }

  const ws = new WebSocket(wsUrl);
  await new Promise((resolve, reject) => {
    ws.on('open', resolve);
    ws.on('error', reject);
  });

  try {
    await sendCommand(ws, 'Page.enable');

    // 3. Navigate to page via HTTP
    console.log(`Loading: ${pageUrl}`);
    const navResult = await sendCommand(ws, 'Page.navigate', { url: pageUrl });
    if (navResult.errorText) throw new Error(`Navigation failed: ${navResult.errorText}`);

    // Wait for load
    await new Promise((resolve) => {
      const handler = (data) => {
        const msg = JSON.parse(data.toString());
        if (msg.method === 'Page.loadEventFired') {
          ws.removeListener('message', handler);
          resolve();
        }
      };
      ws.on('message', handler);
    });

    // Extra render wait
    await sleep(3000);

    // 4. Print to PDF
    console.log('Printing PDF...');
    const pdfData = await sendCommand(ws, 'Page.printToPDF', {
      landscape: false,
      displayHeaderFooter: false,
      printBackground: true,
      preferCSSPageSize: true,
      generateDocumentOutline: true,
      marginTop: 0.7,
      marginBottom: 0.7,
      marginLeft: 0.6,
      marginRight: 0.6,
      scale: 1.0,
    });

    const buf = Buffer.from(pdfData.data, 'base64');
    fs.writeFileSync(pdfAbs, buf);
    console.log(`PDF saved: ${pdfAbs} (${(buf.length / 1024).toFixed(1)} KB)`);

  } finally {
    ws.close();
    browserProc.kill();
    httpServer.close();
  }
}

main().catch(err => {
  console.error('PDF EXPORT FAILED:', err.message);
  process.exit(2);
});
