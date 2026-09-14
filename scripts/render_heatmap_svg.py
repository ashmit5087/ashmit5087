from urllib.request import Request, urlopen
import re
from pathlib import Path

USERNAME = "ashmit5087"
URL = f"https://github.com/users/{USERNAME}/contributions"
OUT = Path("assets/contrib-heatmap.svg")

req = Request(URL, headers={"User-Agent": "github-profile-generator"})
html = urlopen(req, timeout=20).read().decode("utf-8")
pattern = r'<td[^>]*class="[^"]*ContributionCalendar-day[^"]*"[^>]*data-date="([^"]+)"[^>]*data-level="(\\d)"[^>]*>'
cells = re.findall(pattern, html)
if not cells:
    raise RuntimeError("Could not parse GitHub contribution calendar.")

vals = [int(level) for _, level in cells[-371:]]
while len(vals) < 371:
    vals.insert(0, 0)

cell_w, cell_h, gap, cols, rows = 12, 12, 3, 53, 7
width, height = cols*(cell_w+gap)+20, rows*(cell_h+gap)+48
rects = []
for i, level in enumerate(vals):
    x = 10 + (i//rows)*(cell_w+gap)
    y = 32 + (i%rows)*(cell_h+gap)
    opacity = [0.08,0.25,0.45,0.68,0.95][min(level,4)]
    rects.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" rx="2" fill="currentColor" opacity="{opacity}"/>')

svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {w} {h}">
<style>.t{{font-family:"Courier New",Consolas,monospace;fill:currentColor}}
.r{{animation:glow 2.4s ease-in-out infinite}}
@keyframes glow{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}</style>
<text x="10" y="18" class="t" font-size="13">github activity • {user}</text>
<g class="r">{rects}</g>
</svg>""".format(w=width, h=height, user=USERNAME, rects="".join(rects))

OUT.write_text(svg, encoding="utf-8")
print(f"Wrote {OUT}")
