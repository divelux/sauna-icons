// Renders preview.png and preview-dark.png (contact sheets). Usage: NODE_PATH=<dir with playwright> node preview.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const root = path.join(__dirname, '..');
const meta = JSON.parse(fs.readFileSync(path.join(root, 'icons.json'), 'utf8'));
const b64 = (p) => fs.readFileSync(p).toString('base64');
const BRIC = path.join(__dirname, '..', '..', '_fonts', 'BricolageGrotesque-Bold.ttf');
const INTER = path.join(__dirname, '..', '..', '_fonts', 'Inter-Regular.ttf');
function page(dark) {
  const bg = dark ? '#1c110b' : '#f6f3ee', ink = dark ? '#f6f3ee' : '#1b1512', mut = dark ? '#b9aea3' : '#6f655c', line = dark ? '#3a2a20' : '#e3ddd3';
  const cells = meta.icons.map((i) => {
    const svg = fs.readFileSync(path.join(root, i.file), 'utf8').replace('width="24" height="24"', 'width="64" height="64"').replace(/<title>.*?<\/title>/, '');
    return `<div class="c">${svg}<span>${i.name}</span></div>`;
  }).join('');
  const small = meta.icons.map((i) => fs.readFileSync(path.join(root, i.file), 'utf8').replace(/<title>.*?<\/title>/, '')).join('');
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  @font-face{font-family:B;src:url(data:font/ttf;base64,${b64(BRIC)})}
  @font-face{font-family:I;src:url(data:font/ttf;base64,${b64(INTER)})}
  body{margin:0;background:${bg};color:${ink};font-family:I,sans-serif;width:1600px}
  .w{padding:56px 64px 48px}
  h1{font:700 54px/1.05 B,sans-serif;margin:0 0 10px;letter-spacing:-.01em}
  p{margin:0 0 36px;color:${mut};font-size:22px}
  .g{display:grid;grid-template-columns:repeat(9,1fr);border-top:1px solid ${line};border-left:1px solid ${line}}
  .c{display:flex;flex-direction:column;align-items:center;gap:14px;padding:26px 4px 18px;border-right:1px solid ${line};border-bottom:1px solid ${line}}
  .c span{font-size:13px;color:${mut}}
  .s{display:flex;flex-wrap:wrap;gap:17px;margin-top:30px;align-items:center}
  .f{display:flex;justify-content:space-between;margin-top:30px;color:${mut};font-size:18px}
  </style></head><body><div class="w"><h1>Sauna &amp; Banya Icon Set</h1>
  <p>36 line icons · 24 px grid · 1.5 px stroke · SVG · free under CC BY 4.0</p>
  <div class="g">${cells}</div><div class="s">${small}</div>
  <div class="f"><span>Actual size, 24 px, above</span><span>Made by DIVELUX — diveluxsaunahat.com</span></div></div></body></html>`;
}
(async () => {
  const browser = await chromium.launch();
  try {
    const pg = await browser.newPage({ viewport: { width: 1600, height: 900 } });
    for (const dark of [false, true]) {
      await pg.setContent(page(dark));
      await pg.screenshot({ path: path.join(root, dark ? 'preview-dark.png' : 'preview.png'), fullPage: true });
    }
  } finally { await browser.close(); }
})();
