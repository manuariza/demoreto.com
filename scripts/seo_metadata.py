"""Technical metadata only; preserve visible copy and preview exclusion."""
import html,json,re
from html.parser import HTMLParser
from urllib.parse import urljoin
ORIGIN='https://demoreto.com'
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.images=[]
 def handle_data(self,s):self.parts.append(s)
 def handle_starttag(self,t,a):
  if t=='img':self.images.append(dict(a))
def metadata(path,title,body,base='/new-design/'):
 e=lambda s:html.escape(str(s),quote=True)
 url=ORIGIN+base+(path.strip('/')+'/' if path else '')
 parser=Text();parser.feed(body)
 clean=' '.join(' '.join(parser.parts).split())
 descriptions={
 '':'Conservación y restauración de obras de arte en Madrid. Conozca las intervenciones del estudio DeMoreto y la pintura de Antonio G. Ariza.',
 'restauracion':'Restauración de pintura, escultura y patrimonio artístico en Madrid. Intervenciones documentadas con imágenes y procesos del estudio DeMoreto.',
 'obra':'La obra pictórica de Antonio G. Ariza: dieciséis pinturas con imágenes completas, detalles de la superficie y vistas en el espacio.',
 'estudio':'Antonio G. Ariza, restaurador, historiador del arte y pintor. Formación, investigación y práctica de conservación en el estudio DeMoreto de Madrid.',
 'contacto':'Contacte con el estudio DeMoreto en Madrid para consultar una restauración o conocer la obra de Antonio G. Ariza. Visitas con cita previa.',
 'archivo':'Archivo del estudio DeMoreto: restauraciones, procesos y notas de historia del arte, con las publicaciones y secuencias originales del taller.'}
 description=descriptions.get(path)
 if description is None:
  if path.startswith('obra/'):description=f'{title}, obra de Antonio G. Ariza. Vea la pintura completa, detalles de su superficie y su presentación en el espacio. Consultas al estudio DeMoreto.'
  else:
   match=re.search(r'<div class="case-intro">.*?<p>(.*?)</p>',body,re.S)
   source=html.unescape(re.sub('<[^>]+>',' ',match.group(1))) if match else clean
   description=source if len(source)<=165 else source[:162].rsplit(' ',1)[0]+'…'
 fulltitle=('Restauración de arte en Madrid | DeMoreto' if not path else f'{title} — '+('Antonio G. Ariza | DeMoreto' if path.startswith('obra/') else 'DeMoreto'))
 first=next((i for i in parser.images if i.get('src')),{'src':base+'assets/studio-2.webp','alt':'El taller DeMoreto'})
 image=urljoin(ORIGIN,first['src'])
 personid=ORIGIN+'/#antonio-g-ariza';serviceid=ORIGIN+'/#service';siteid=ORIGIN+base+'#website'
 graph=[{'@type':'WebSite','@id':siteid,'url':ORIGIN+base,'name':'DeMoreto','inLanguage':'es','publisher':{'@id':serviceid}},
 {'@type':'Person','@id':personid,'name':'Antonio G. Ariza','jobTitle':'Restaurador, historiador del arte y pintor','url':ORIGIN+base+'estudio/','worksFor':{'@id':serviceid}},
 {'@type':'ProfessionalService','@id':serviceid,'name':'DeMoreto','url':ORIGIN+base,'email':'agariza@gmail.com','address':{'@type':'PostalAddress','addressLocality':'Madrid','addressCountry':'ES'},'sameAs':['https://www.instagram.com/moreto_restauracion/']},
 {'@type':'WebPage','@id':url+'#webpage','url':url,'name':fulltitle,'description':description,'inLanguage':'es','isPartOf':{'@id':siteid},'about':{'@id':serviceid},'primaryImageOfPage':{'@type':'ImageObject','url':image}}]
 if path.startswith('obra/'):
  work={'@type':'VisualArtwork','@id':url+'#artwork','name':title,'url':url,'image':image,'creator':{'@id':personid},'artform':'Pintura'};graph.append(work);graph[3]['mainEntity']={'@id':work['@id']}
 if path:
  crumbs=[{'@type':'ListItem','position':1,'name':'DeMoreto','item':ORIGIN+base}]
  parts=path.split('/')
  if len(parts)>1:crumbs.append({'@type':'ListItem','position':2,'name':{'obra':'Obra de Antonio','restauracion':'Restauración','archivo':'Archivo del estudio'}.get(parts[0],parts[0]),'item':ORIGIN+base+parts[0]+'/'})
  crumbs.append({'@type':'ListItem','position':len(crumbs)+1,'name':title,'item':url})
  graph.append({'@type':'BreadcrumbList','@id':url+'#breadcrumbs','itemListElement':crumbs});graph[3]['breadcrumb']={'@id':url+'#breadcrumbs'}
 tags=f'<title>{e(fulltitle)}</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{e(url)}"><meta name="theme-color" content="#f7f5ef">'
 for prop,val in [('type','website'),('locale','es_ES'),('site_name','DeMoreto'),('title',fulltitle),('description',description),('url',url),('image',image),('image:alt',first.get('alt',title))]:tags+=f'<meta property="og:{prop}" content="{e(val)}">'
 tags+=f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(fulltitle)}"><meta name="twitter:description" content="{e(description)}"><meta name="twitter:image" content="{e(image)}">'
 tags+='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')+'</script>'
 return tags
