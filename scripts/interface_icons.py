"""Render interface symbols consistently without platform emoji fonts."""
import re
PATHS={
 '↗':('external','M5 19 19 5M5 5h14v14'),
 '→':('next','M4 12h16m-7-7 7 7-7 7'),
 '↓':('down','M12 4v16m-7-7 7 7 7-7'),
 '☰':('menu','M4 7h16M4 12h16M4 17h16'),
 '▷':('play','m7 4 13 8-13 8Z'),
}
def icon(symbol):
 name,path=PATHS[symbol]
 return f'<svg class="ui-icon ui-icon-{name}" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="{path}"/></svg>'
def render_icons(document):
 parts=re.split(r'(<[^>]+>)',document);raw=False
 for i,part in enumerate(parts):
  if part.startswith('<'):
   if re.match(r'<(?:script|style)\b',part):raw=True
   elif re.match(r'</(?:script|style)\b',part):raw=False
  elif not raw:
   for symbol in PATHS:part=part.replace(symbol,icon(symbol))
   parts[i]=part
 return ''.join(parts)
