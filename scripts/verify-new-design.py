from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,hashlib,subprocess
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'new-design';errors=[]
class Check(HTMLParser):
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  for k in ['href','src','poster']:
   url=d.get(k,'');path=unquote(urlparse(url).path)
   if url.startswith('/') and not url.startswith('//'):
    target=ROOT/path.lstrip('/')
    if path.endswith('/'):target=target/'index.html'
    if not target.exists():errors.append(f'{self.file}: missing {url}')
  if tag=='img' and 'alt' not in d:errors.append(f'{self.file}: missing alt')
for file in out.rglob('*.html'):
 p=Check();p.file=str(file.relative_to(ROOT));p.feed(file.read_text())
posts=json.load(open(ROOT/'reports/content-archive/instagram.json'));by={p['code']:p for p in posts};links=json.load(open(ROOT/'reports/content-archive/all-public-links.json'));media_count=0;videos=0;no_caption=0
for p in by.values():
 if p.get('status')!='public-data-found':errors.append('Unarchived post '+p['code']);continue
 if not p.get('caption'):no_caption+=1
 if not (out/'archivo'/p['code']/'index.html').exists():errors.append('Missing archive page '+p['code'])
 raw=p.get('raw',{});expected=raw.get('carousel_media_count') or len(raw.get('carousel_media',[])) or len(raw.get('edge_sidecar_to_children',{}).get('edges',[])) or p.get('expected_media_count',1)
 if len(p['media'])!=expected:errors.append('Carousel count mismatch '+p['code'])
 p['expected_media_count']=expected
 for m in p['media']:
  f=out/'assets/restoration'/m.get('file','missing');media_count+=1
  if not f.is_file():errors.append('Missing '+str(f));continue
  m['sha256']=hashlib.sha256(f.read_bytes()).hexdigest();m['bytes']=f.stat().st_size
  if m['type']=='image':
   with Image.open(f) as im:im.verify()
  else:
   videos+=1
   probe=subprocess.run(['/opt/homebrew/bin/ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(f)],capture_output=True,text=True)
   try:m['duration_seconds']=float(probe.stdout)
   except ValueError:errors.append('Invalid video '+str(f))
 if raw:
  for child in raw.get('carousel_media',[raw]):
   if child.get('media_type')==2 and not child.get('video_versions') and not child.get('video_url'):errors.append('Video URL absent '+p['code'])
 if 'raw' in p:del p['raw']
 p.pop('text',None)
 for m in p.get('media',[]):m.pop('src',None)
ordered=[by[x['url'].rstrip('/').split('/')[-1]] for x in links if x['url'].rstrip('/').split('/')[-1] in by]
if len(ordered)!=len(links):errors.append('Feed reconciliation mismatch')
(ROOT/'reports/content-archive/instagram.json').write_text(json.dumps(ordered,ensure_ascii=False,indent=2))
report={'pages':len(list(out.rglob('index.html'))),'public_posts_discovered':len(links),'posts_archived':len([p for p in by.values()if p['status']=='public-data-found']),'media_files':media_count,'images':media_count-videos,'videos':videos,'captionless_posts':no_caption,'errors':errors}
(ROOT/'reports/content-archive/verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
