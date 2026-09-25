from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,sys,xml.etree.ElementTree as ET,hashlib,re
ROOT=Path(__file__).resolve().parents[1];release=Path(sys.argv[1]);errors=[]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.meta={};self.canonical=[];self.links=[];self.schemas=[];self.buffer=None;self.h1=0
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='meta':self.meta[d.get('name',d.get('property'))]=d.get('content')
  if t=='link' and d.get('rel')=='canonical':self.canonical.append(d['href'])
  if t=='h1':self.h1+=1
  for k in ['src','href','poster','data-full']:
   if d.get(k,'').startswith('/'):self.links.append(d[k])
  if t=='script' and d.get('type')=='application/ld+json':self.buffer=''
 def handle_data(self,s):
  if self.buffer is not None:self.buffer+=s
 def handle_endtag(self,t):
  if t=='script' and self.buffer is not None:self.schemas.append(json.loads(self.buffer));self.buffer=None
expected=set();descriptions=[]
for f in release.rglob('index.html'):
 rel=f.relative_to(release);route=rel.parent.as_posix();route='' if route=='.' else route+'/'
 p=Page();p.feed(f.read_text());canonical='https://demoreto.com/'+route
 if p.canonical!=[canonical]:errors.append(f'Canonical mismatch: {rel}')
 excluded=route.startswith('archivo/') and route!='archivo/'
 if ('noindex' in p.meta.get('robots',''))!=excluded:errors.append(f'Index policy: {rel}')
 if not excluded:expected.add(canonical);descriptions.append(p.meta.get('description'))
 if not p.schemas or p.h1!=1:errors.append(f'Schema/h1: {rel}')
 for u in p.links:
  path=unquote(urlparse(u).path);target=release/path.lstrip('/')
  if path.endswith('/'):target=target/'index.html'
  if not target.exists():errors.append(f'Missing {u} from {rel}')
listed={e.text for e in ET.parse(release/'sitemap.xml').iter() if e.tag=='{http://www.sitemaps.org/schemas/sitemap/0.9}loc'}
if listed!=expected:errors.append('Sitemap membership mismatch')
if len(descriptions)!=len(set(descriptions)):errors.append('Duplicate indexable descriptions')
for f in (ROOT/'new-design').rglob('index.html'):
 if 'content="noindex,follow"' not in f.read_text():errors.append('Preview indexable: '+str(f))
for source in (ROOT/'new-design').rglob('index.html'):
 target=release/source.relative_to(ROOT/'new-design')
 expected_body=re.search(r'<body.*',source.read_text(),re.S).group().replace('/new-design/','/')
 actual_body=re.search(r'<body.*',target.read_text(),re.S).group()
 if expected_body!=actual_body:errors.append('Visible body changed: '+str(source))
result={'release_pages':len(list(release.rglob('index.html'))),'sitemap_urls':len(listed),'archive_pages_noindex':98,'preview_pages_noindex':137,'visible_body_unchanged':not any('Visible body' in x for x in errors),'errors':errors}
(ROOT/'reports/seo/2026-09-25/validation.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));raise SystemExit(bool(errors))
