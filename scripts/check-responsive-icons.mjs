import {chromium} from '/Users/manuariza/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'node:fs';
const dir='/Users/manuariza/Sites/demoreto.com/reports/responsive-icons';fs.mkdirSync(dir,{recursive:true});
const b=await chromium.launch({headless:true,executablePath:'/Users/manuariza/Library/Caches/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-mac-arm64/chrome-headless-shell'});
const results=[];
for(const [name,width,height] of [['small-phone',320,740],['iphone-se',375,667],['iphone',390,844],['android',412,915],['iphone-max',430,932],['ipad',768,1024],['ipad-air',820,1180],['ipad-landscape',1180,820],['desktop',1440,1000]]){
 const p=await b.newPage({viewport:{width,height},reducedMotion:'reduce',isMobile:width<1180,hasTouch:width<1180});
 const errors=[];p.on('pageerror',e=>errors.push(e.message));
 for(const route of ['/','/obra/','/restauracion/','/obra/sunset-3/','/restauracion/florero-baudesson/','/contacto/','/estudio/']){
 await p.goto('http://localhost:8765'+route,{waitUntil:'load'});
 const state=await p.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,unicode:[...document.body.innerText].filter(c=>/[↗→↓☰▷💪🎨]/u.test(c)),icons:document.querySelectorAll('.ui-icon').length}));
 results.push({name,route,...state,errors:[...errors]});
 if(route==='/'){await p.locator('img').evaluateAll(es=>es.forEach(i=>i.loading='eager'));await p.locator('img').evaluateAll(es=>Promise.all(es.filter(i=>i.src).map(i=>i.decode().catch(()=>{}))));await p.screenshot({path:`${dir}/${name}-home.png`,fullPage:true});if(width<=700){await p.locator('.menu-toggle').click();if(await p.locator('#mobile-nav').isHidden())throw Error('Menu failed '+name);await p.screenshot({path:`${dir}/${name}-menu.png`});await p.locator('.menu-toggle').click();}}
 if(route==='/contacto/')await p.screenshot({path:`${dir}/${name}-contact.png`,fullPage:true});
 }
 await p.close();
}
await b.close();fs.writeFileSync(dir+'/checks.json',JSON.stringify(results,null,2));
const failed=results.filter(r=>r.overflow||r.unicode.length||r.errors.length||!r.icons);console.log(JSON.stringify({checks:results.length,failures:failed},null,2));process.exitCode=failed.length?1:0;
