import json
from pathlib import Path
d=json.loads(Path('data/contributions.json').read_text()); vals=[x['level'] for x in d['days'][-371:]]; vals=[0]*(371-len(vals))+vals
pal=['#161b22','#0e4429','#006d32','#26a641','#39d353','#69f0a0']; cw=ch=11; gap=3; cols=53; rows=7; x0=12; y0=45; W=x0+cols*(cw+gap)+12; H=y0+rows*(ch+gap)+68
rect=[]
for i,l in enumerate(vals):
 c,r=divmod(i,7); x=x0+c*(cw+gap); y=y0+r*(ch+gap); rect.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="2" fill="{pal[min(max(l,0),5)]}" class="cell" style="animation-delay:{(c+r)*.018:.3f}s"/>')
legend=''.join(f'<rect x="{W-115+i*18}" y="{H-22}" width="12" height="12" rx="2" fill="{c}"/>' for i,c in enumerate(pal)); footer=f"{d.get('total',0):,} contributions • current streak {d.get('current_streak',0)}d • longest {d.get('longest_streak',0)}d"
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><style>.t{{font-family:"Courier New",Consolas,monospace;fill:#c9d1d9}}.sub{{font-family:"Courier New",Consolas,monospace;fill:#8b949e}}.cell{{opacity:0;transform:translateY(-8px);animation:drop .38s ease-out forwards}}@keyframes drop{{to{{opacity:1;transform:translateY(0)}}}}</style><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="#0d1117" stroke="#30363d"/><text x="12" y="23" class="t" font-size="13">ashmit@github ~ $ ./contributions.sh</text><text x="12" y="37" class="sub" font-size="10">last year • real GitHub activity</text><g>{''.join(rect)}</g><text x="12" y="{H-12}" class="sub" font-size="10">{footer}</text><text x="{W-142}" y="{H-30}" class="sub" font-size="9">Less</text><g>{legend}</g><text x="{W-20}" y="{H-12}" class="sub" font-size="9" text-anchor="end">More</text></svg>'''
Path('assets/contrib-heatmap.svg').write_text(svg)
