import json,re
from pathlib import Path
import requests
from bs4 import BeautifulSoup
u='ashmit5087'; out=Path('data/contributions.json')
r=requests.get(f'https://github.com/users/{u}/contributions',headers={'User-Agent':'Mozilla/5.0'},timeout=30); r.raise_for_status(); s=BeautifulSoup(r.text,'html.parser')
days=[]; counts={}
for c in s.select('td.ContributionCalendar-day'):
 d=c.get('data-date'); lvl=c.get('data-level')
 if d and lvl is not None:
  days.append({'date':d,'level':int(lvl)}); m=re.search(r'([\d,]+) contribution',c.get('aria-label','')); counts[d]=int(m.group(1).replace(',','')) if m else 0
days.sort(key=lambda x:x['date']); run=longest=0
for d in sorted(counts):
 if counts[d]: run+=1; longest=max(longest,run)
 else: run=0
p={'username':u,'days':days,'counts':counts,'total':sum(counts.values()),'current_streak':run,'longest_streak':longest}; out.parent.mkdir(exist_ok=True); out.write_text(json.dumps(p,indent=2)); print('wrote',out)
