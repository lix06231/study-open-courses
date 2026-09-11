# Build & PDF 工程适配与踩坑清单

实战两门课（`AI for Everyone` 的 `course-pack/`、`Generative AI for Everyone` 的 `course-pack-genai/`）沉淀出的构建/导出经验。**这些是"把 Markdown 真正变成能交付的 HTML + PDF"时最容易踩的坑**，属于工程适配层，与 `publishing-spec.md`（结构规范层）配套阅读。

当前默认路线：`scripts/build_course_book.py` 会生成临时打印副本，把所有 `<details>` 强制展开，再用浏览器导出 PDF；交互版 HTML 保持折叠。需要 CDP 文档大纲、Tagged PDF 或备用渲染器时，使用仓库内实际存在的 `scripts/export_pdf_cdp.js`。下面保留的旧项目脚本名是历史案例，不是本 Skill 的必需文件。

```
build_course_book.py  (Markdown → HTML)  →  course-book.html（保持 <details> 折叠交互）
                                    │  交付版，不动
                                    ▼
自动生成 .print-tmp.html，并为 `<details>` 添加 `open`
                                    │
                                    ▼
浏览器 CLI；需要 CDP 特性时改用 export_pdf_cdp.js
```

---

## 1. Markdown → HTML 构建（`build_course_book.py`）

### 1.1 `<details>` 必须用「占位符延迟替换」，不能在行内阶段转义

`<details>` / `<summary>` / `<br>` 是原始 HTML 标签，**不能**在 `esc()`（HTML 转义）之后才识别，否则会被转义成 `&lt;details&gt;` 失效。正确做法：

```python
# 先把 <details>...</details> 整块挖出来，用占位符替换
details_blocks = re.findall(r'<details>.*?</details>', md, re.S)
md_no_details = re.sub(r'<details>.*?</details>', 'DETAILSPLACEHOLDER', md, flags=re.S)
# 逐行转换时遇到占位符，再单独 convert_details(details_blocks[n])
```

`convert_details` 内部：先取 `<summary>...</summary>`，剩余 body 再递归 `convert_blocks()`。**注意 `<details>` 的 body 里可能还有列表/表格/图片**，要复用完整的块级转换。

### 1.2 `<br>` 续行解析：拆成 `inline_plain` + `inline`

列表项/段落里常有 `<br>` 换行。行内转换分两层：

```python
def inline_plain(text):   # 不含 <br>：先 esc 再处理 `code` / **bold** / [text](url)
def inline(text):         # 先按 <br> 切分，非 <br> 段交给 inline_plain，<br> 原样保留
    parts = re.split(r'(<br\s*/?>)', text)
    ...
```

列表解析还要**把 `<br>` 开头的行追加到当前 `<li>`**（否则会多出一个空段落）：

```python
while i < len(lines) and lines[i].strip().startswith('<br'):
    item += inline(lines[i].strip()); i += 1
```

### 1.3 `%` 格式化冲突 → 用字符串拼接

用 `'...%s...' % (x)` 拼接大段 HTML 时，正文里的 CSS 花括号或 `%` 会被当占位符报错（如 `data:image/svg+xml;base64,...` 里的 `%`）。**改用 `+` 字符串拼接或 `''.join()`，或转义为 `%%`**。构建脚本里尽量统一用拼接，避免大模板 `%` 格式化的隐藏坑。

### 1.4 其他易漏的块级规则

- **表格行 `|` 优先于段落**：`s.startswith('|')` 要在普通段落之前判断。
- **有序/无序列表区分**：有序 `^\d+[\.、]\s+`（注意中文顿号 `、` 也常被当列表序号），无序 `^[-*]\s+`。
- **图片**：`![alt](src)` → `<figure><img src="..." alt="..." loading="lazy"></figure>`（`loading="lazy"` 会触发 PDF 懒加载问题，见 §3.2）。
- **slug 规则**（锚点 id，必须和上一门课一致，否则目录链接断裂）：非 `[a-z0-9\u4e00-\u9fff]` 一律替换为 `-`，折叠连续 `-`，去首尾 `-`，ASCII 转小写。中文标题保留原字符。

---

## 2. `<details>` 的 HTML 与 PDF 分流

交付的 standalone HTML 保留 `<details>` 折叠交互。`build_course_book.py` 在打印前生成 `.print-tmp.html`，只给临时副本中的 `<details>` 增加 `open`，确保答案进入 PDF；导出结束后删除临时文件。

不要为每门课复制并改写一份转换脚本。若产品确实要求“正文问题跳转到文末答案附录”，将它视为单独的版式需求并进行专项实现和回归；它不是标准课程包的必要路径。

---

## 3. PDF 导出（`build_course_book.py` / `export_pdf_cdp.js`）

### 3.1 选择路径

默认使用 `build_course_book.py` 的浏览器 CLI 路径，它会生成两遍 PDF 以校准目录页码，并在可用时注入书签。需要直接控制 CDP `Page.printToPDF` 或把 CLI 故障与页面故障分开诊断时，改用仓库内的 `scripts/export_pdf_cdp.js`。当前脚本启用背景和文档大纲，不提供自定义页眉；不要声称未实现的版式能力。

### 3.2 图片懒加载：PDF 会丢图

`<img loading="lazy">` 在 headless 打印时可能不渲染。默认构建器会在打印副本中改为 `loading="eager"`，并给浏览器设置布局与等待预算。若改用其他渲染器，仍需等待字体和图片完成：

```javascript
// 1) 全部改成 eager
document.querySelectorAll('img').forEach(i => { i.loading = 'eager'; });
// 2) await document.fonts.ready（等字体）
// 3) fetch 预加载所有图片 URL 到浏览器缓存
// 4) 轮询 img.complete && img.naturalWidth > 0 直到全部加载完
// 5) 再给 1500ms 让布局稳定
```

### 3.3 本地页面加载

CDP 脚本通过临时本地 HTTP 服务加载指定 HTML，避免把 `file:///` 路径写入输出。把要打印的实际 HTML 路径直接传给脚本；不要靠课程文件名的字符串替换寻找临时文件。

### 3.4 Edge profile 目录 + CDP 端口隔离（多门课/多次构建必踩）

- **每门课独立 `--user-data-dir`**（如 `course-pack-genai/scripts/.edge-profile`），否则同目录 profile 会被锁、二次启动直接失败。
- **CDP 端口隔离**：上一门课用了 9224/9231，第二门课要用不同端口（如 9232），否则并行/连跑会撞端口。
- Windows 下浏览器路径写绝对路径（`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`）；Python 解释器也写绝对路径（managed venv）。

---

## 4. SVG 静态越界检查（text-anchor 大坑）

用 `gen_svg_check.py` 生成 `svg-check.html`（把全部 SVG 内联 + 一段 `collect()` JS），再用 CDP 打开页面读取 `window.__overflow`，用 `getBBox()` 检测文字是否超出其所在 `rect` 或 `viewBox`。

### 4.1 核心坑：`text-anchor` 的 middle/end 锚点会误报

SVG 文字有 `text-anchor="start|middle|end"`。**middle/end 锚点的 `getBBox()` 原点落在锚点位置，直接拿 bbox 和 rect 比较会大面积误报**（实战初版误报 16 张，全是因为没区分锚点）。

正确做法：**用文字 bbox 的「中心点」判断它落在哪个 rect 内，再算四边溢出**：

```javascript
const tc = { x: tb.x + tb.width/2, y: tb.y + tb.height/2 };  // 中心点
const host = rects.find(r => tc.x>=r.b.x && tc.x<=r.b.x+r.b.width && tc.y>=r.b.y && tc.y<=r.b.y+r.b.height);
// 再用 bbox 四边 vs rect 四边算 overL/overR/overT/overB
```

真实越界案例：轴标签「占该职能支出比例 →」用 `middle` 锚点，右侧溢出 11px → 改 `text-anchor="end"` 修复。

### 4.2 判定阈值

- `> 0.5px` 记「溢出」，`> -3px` 记「贴边」——小阈值别设太死，否则轴标签正常贴边也会刷屏。

---

## 5. 结构完整性标准（两门课通用，最容易漏）

这是「教材标准」的强制组成部分，**不是可有可无的加分项**。第二门课一开始就漏了二三四章综合练习和全书结语，最后补齐：

- **每节**含：问题与目的 / 课程讲解 / 推理路径 / 重要例子 / 适用边界与常见误区 / 即时理解检查（`<details>` 折叠）/ 迁移练习（`<details>` 折叠）/ 证据定位。
- **`[Course teaching]` vs `[AI explanation]` 双标签**：严格区分「课程原文重述」和「AI 新增解释」，build 时转成 `.provenance` 框。
- **每章末尾**有「综合练习」（概念映射 / 局限识别 / 自测，答案用 `<details>`）。
- **全书末尾**有「结语 · 致读者」。

交付前用 `checklist` 过一遍：每章有没有综合练习？全书有没有结语？`<details>` 数量对不对？（第二门课 4 章 37 节、76 个 `<details>`、22 张 figure，构建脚本末尾打印统计用于核对。）
