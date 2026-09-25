import { chromium } from '/Users/manuariza/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'node:fs/promises';
const root=process.cwd(), out=root+'/reports/content-archive';
const browser=await chromium.launch({headless:true,executablePath:'/Users/manuariza/Library/Caches/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-mac-arm64/chrome-headless-shell'});
const context=await browser.newContext();
const seeds=JSON.parse(await fs.readFile(root+'/reports/content-archive/all-public-links.json'));
const found=new Map();
function walk(x){if(!x||typeof x!=='object')return;if(x.shortcode && (x.display_url||x.image_versions2||x.carousel_media||x.edge_sidecar_to_children))found.set(x.shortcode,x);if(x.code&&(x.image_versions2||x.video_versions||x.carousel_media))found.set(x.code,x);for(const v of Object.values(x))if(typeof v==='object')walk(v)}
const p=await context.newPage();p.on('response',async r=>{try{if((r.headers()['content-type']||'').includes('json'))walk(await r.json())}catch{}});
const records=JSON.parse(await fs.readFile(out+'/instagram.json'));const done=new Set(records.filter(r=>r.status==='public-data-found').map(r=>r.code));
for(const item of [{url:'https://www.instagram.com/moreto_restauracion/'},...seeds]){
 const code=item.url.match(/\/(?:p|reel)\/([^/]+)/)?.[1];
 if(code&&done.has(code))continue;
 try{await p.goto(item.url,{waitUntil:'domcontentloaded',timeout:30000});await p.waitForTimeout(1600);
 const decline=p.getByRole('button',{name:'Decline optional cookies',exact:true});if(await decline.isVisible())await decline.click();
 for(const s of await p.locator('script[type="application/json"]').allTextContents()){try{walk(JSON.parse(s))}catch{}}
 const raw=found.get(code);const text=await p.locator('body').innerText();
 if(!code){await fs.writeFile(out+'/profile.txt',text);continue;}
 const record={code,url:item.url,expected_media_count:raw?(raw.carousel_media_count||raw.carousel_media?.length||raw.edge_sidecar_to_children?.edges?.length||1):0,media:[],status:raw?'public-data-found':'public-data-unavailable'};
 if(raw){
  const children=raw.carousel_media||raw.edge_sidecar_to_children?.edges?.map(e=>e.node)||[raw];
  record.caption=typeof raw.caption==='string'?raw.caption:raw.caption?.text||raw.edge_media_to_caption?.edges?.[0]?.node?.text||'';
  record.timestamp=raw.taken_at||raw.taken_at_timestamp;
  let n=0;for(const child of children){n++;const video=child.video_url||child.video_versions?.[0]?.url;const src=video||child.display_url||child.image_versions2?.candidates?.[0]?.url;const media={order:n,type:video?'video':'image',src,width:child.original_width||child.dimensions?.width,height:child.original_height||child.dimensions?.height};
   if(src){try{const r=await context.request.get(src);if(!r.ok())throw Error(String(r.status()));const name=code+'-'+String(n).padStart(2,'0')+(video?'.mp4':'.jpg');await fs.writeFile(root+'/new-design/assets/restoration/'+name,await r.body());media.file=name;media.status='downloaded'}catch(e){media.status='failed';media.error=e.message}}record.media.push(media);
  }
 }
 const old=records.findIndex(r=>r.code===code);if(old>=0)records[old]=record;else records.push(record);await fs.writeFile(out+'/instagram.json',JSON.stringify(records,null,2));console.log(code,record.status,record.media.length);
 }catch(e){records.push({code,url:item.url,status:'failed',error:e.message});console.log(code,e.message)}
}
await fs.writeFile(out+'/instagram.json',JSON.stringify(records,null,2));await browser.close();
