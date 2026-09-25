"""Prepare a root-URL release in a separate directory; never deploy it.
Usage: python3 scripts/prepare-search-release.py /tmp/demoreto-release
"""
from pathlib import Path
import sys,re,shutil,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];source=ROOT/'new-design'
if len(sys.argv)!=2:raise SystemExit('Supply a new, empty output directory outside the repository.')
out=Path(sys.argv[1]).resolve()
if out==ROOT or ROOT in out.parents:raise SystemExit('Output must be outside the repository.')
if out.exists() and any(out.iterdir()):raise SystemExit('Output directory must be empty.')
out.mkdir(parents=True,exist_ok=True)
urls=[];mapping=[];images={}
for p in source.rglob('index.html'):
 rel=p.relative_to(source);route=rel.parent.as_posix();route='' if route=='.' else route+'/'
 text=p.read_text().replace('/new-design/','/')
 archive=route.startswith('archivo/') and route!='archivo/'
 if not archive:text=text.replace('content="noindex,follow"','content="index,follow,max-image-preview:large"')
 dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text)
 if not archive:
  canonical='https://demoreto.com/'+route;urls.append(canonical)
  match=re.search(r'<meta property="og:image" content="([^"]+)">',text)
  if match:images[canonical]=match.group(1)
 mapping.append(f'/new-design/{route}\thttps://demoreto.com/{route}\t'+('noindex,follow' if archive else 'index,follow'))
for name in ['style.css','site.js']:(out/name).write_text((source/name).read_text().replace('/new-design/','/'))
# Only distribute assets referenced by HTML/CSS/JS, including full-resolution zoom images.
assets=set()
for p in out.rglob('*'):
 if p.is_file() and p.suffix in ['.html','.css','.js']:
  assets.update(re.findall(r'/assets/([^\s\"\'<>?#)]+)',p.read_text()))
for asset in assets:
 src=source/'assets'/asset
 if not src.is_file():raise SystemExit('Missing asset '+asset)
 dst=out/'assets'/asset;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
ET.register_namespace('','http://www.sitemaps.org/schemas/sitemap/0.9')
root=ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
ET.register_namespace('image','http://www.google.com/schemas/sitemap-image/1.1')
for url in sorted(urls):
 node=ET.SubElement(root,'url');ET.SubElement(node,'loc').text=url
 if url in images:ET.SubElement(ET.SubElement(node,'{http://www.google.com/schemas/sitemap-image/1.1}image'),'{http://www.google.com/schemas/sitemap-image/1.1}loc').text=images[url]
ET.ElementTree(root).write(out/'sitemap.xml',encoding='UTF-8',xml_declaration=True)
(out/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://demoreto.com/sitemap.xml\n')
(out/'CNAME').write_text('demoreto.com\n');(out/'.nojekyll').touch()
(out/'llms.txt').write_text('# DeMoreto\n\nEstudio de conservación y restauración de arte de Antonio G. Ariza en Madrid.\n\n'+''.join('- '+u+'\n' for u in sorted(urls))+'\nEste índice es informativo; no garantiza inclusión en buscadores o asistentes.\n')
report=ROOT/'reports/seo/2026-09-25';shutil.copy2(out/'sitemap.xml',report/'sitemap-at-launch.xml');(report/'url-mapping.tsv').write_text('preview\tproduction\tindexing\n'+'\n'.join(mapping)+'\n')
print(f'Prepared {len(mapping)} pages, {len(urls)} indexable URLs and {len(assets)} assets in {out}. Not deployed.')
