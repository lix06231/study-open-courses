const sidebar = document.querySelector('.sidebar');
const toggle = document.querySelector('.nav-toggle');
const search = document.querySelector('#toc-search');
const links = [...document.querySelectorAll('nav a')];
toggle?.addEventListener('click', () => sidebar?.classList.toggle('open'));
links.forEach(link => link.addEventListener('click', () => sidebar?.classList.remove('open')));
search?.addEventListener('input', event => {
  const query = event.target.value.trim().toLowerCase();
  links.forEach(link => {
    link.hidden = query && !link.textContent.toLowerCase().includes(query);
  });
});
const observer = new IntersectionObserver(entries => {
  entries.filter(entry => entry.isIntersecting).forEach(entry => {
    links.forEach(link => link.classList.toggle('active', link.hash === '#' + entry.target.id));
  });
}, { rootMargin: '-10% 0px -80% 0px' });
document.querySelectorAll('h1[id], h2[id], h3[id]').forEach(heading => observer.observe(heading));
