const menu=document.querySelector('.menu-toggle'),mobile=document.querySelector('#mobile-nav');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')==='true';menu.setAttribute('aria-expanded',String(!open));mobile.hidden=open;});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){mobile.hidden=true;menu?.setAttribute('aria-expanded','false');}});
const dialog=document.querySelector('#lightbox');let opener;
document.querySelectorAll('.zoom').forEach(button=>button.addEventListener('click',()=>{opener=button;dialog.querySelector('img').src=button.dataset.full;dialog.querySelector('img').alt=button.dataset.caption;dialog.querySelector('p').textContent=button.dataset.caption;dialog.showModal();}));
dialog?.querySelector('button').addEventListener('click',()=>dialog.close());dialog?.addEventListener('click',e=>{if(e.target===dialog)dialog.close()});dialog?.addEventListener('close',()=>opener?.focus());
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));document.querySelectorAll('[data-category]').forEach(card=>card.hidden=button.dataset.filter!=='Todas'&&card.dataset.category!==button.dataset.filter);}));
const emailAction=document.querySelector('#email-action');
if(emailAction){const work=new URLSearchParams(location.search).get('obra');if(work){const subject='Consulta sobre la obra '+work;const url='mailto:agariza@gmail.com?subject='+encodeURIComponent(subject);emailAction.href=url;document.querySelector('#contact-email').href=url;const context=document.querySelector('#enquiry-context');context.textContent='Su consulta: '+work;context.hidden=false;}}
document.querySelector('#copy-email')?.addEventListener('click',async()=>{const status=document.querySelector('#copy-status');try{await navigator.clipboard.writeText('agariza@gmail.com');status.textContent='Dirección copiada.';}catch{status.textContent='Puede seleccionar y copiar la dirección: agariza@gmail.com';const range=document.createRange();range.selectNodeContents(document.querySelector('#contact-email'));const selection=getSelection();selection.removeAllRanges();selection.addRange(range);}});

// Decode the shared illustration atlas before exposing any cells.
async function showEngravingIntro(){
 const motion=matchMedia('(prefers-reduced-motion: reduce)');
 if(!document.body.classList.contains('home')||motion.matches)return;
 const replay=new URLSearchParams(location.search).get('intro')==='1';
 try{if(!replay&&sessionStorage.getItem('demoreto-intro-engravings-v1'))return;}catch{}
 const atlas=new Image();atlas.src='/new-design/assets/loader/engravings.webp';
 let deadline;
 try{await Promise.race([atlas.decode(),new Promise((_,reject)=>{deadline=setTimeout(()=>reject(new Error('Intro timeout')),2200);})]);}
 catch{return;}finally{clearTimeout(deadline);}
 if(motion.matches||document.hidden)return;
 const grid=document.createElement('div');grid.className='intro-grid';grid.setAttribute('aria-hidden','true');
 const columns=innerWidth<=700?3:7;
 const count=columns*(Math.ceil(innerHeight/(innerWidth/columns))+1);
 const motifs=Array.from({length:count},()=>{
  const cell=document.createElement('span');cell.className='intro-cell';
  const motif=document.createElement('i');motif.className='intro-motif';
  motif.dataset.index=String(Math.floor(Math.random()*6));
  motif.style.backgroundPosition=Number(motif.dataset.index)*20+'% 0';
  cell.append(motif);grid.append(cell);return motif;
 });
 document.body.append(grid);
 try{sessionStorage.setItem('demoreto-intro-engravings-v1','1');}catch{}
 let finished=false,phase=0;
 const cycle=setInterval(()=>{
  motifs.forEach((motif,i)=>{if(i%3!==phase%3)return;
   const next=(Number(motif.dataset.index)+1+Math.floor(Math.random()*5))%6;
   motif.dataset.index=String(next);motif.style.backgroundPosition=next*20+'% 0';
  });phase++;
 },240);
 const finish=()=>{
  if(finished)return;finished=true;clearInterval(cycle);clearTimeout(maximum);
  document.removeEventListener('keydown',skip);motion.removeEventListener('change',finish);
  grid.classList.add('is-leaving');setTimeout(()=>grid.remove(),360);
 };
 const skip=e=>{if(e.key==='Escape'||e.key==='Tab')finish();};
 document.addEventListener('keydown',skip);grid.addEventListener('click',finish);
 motion.addEventListener('change',finish,{once:true});
 const maximum=setTimeout(finish,4000);
 const hero=document.querySelector('.hero-art>img');
 Promise.all([new Promise(resolve=>setTimeout(resolve,1500)),hero?.decode().catch(()=>{})]).then(finish);
}
showEngravingIntro();
const statement=document.querySelector('.manifesto');if(statement&&!matchMedia('(prefers-reduced-motion: reduce)').matches){let busy=false;addEventListener('scroll',()=>{if(busy)return;busy=true;requestAnimationFrame(()=>{const offset=Math.max(-25,Math.min(25,(statement.getBoundingClientRect().top-innerHeight/2)*.035));statement.querySelectorAll('p').forEach((p,i)=>p.style.transform='translateX('+(i?offset:-offset)+'px)');busy=false;});},{passive:true});}
const search=document.querySelector('#archive-search');search?.addEventListener('input',()=>{const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();const term=normalize(search.value);let count=0;document.querySelectorAll('[data-search]').forEach(card=>{card.hidden=!normalize(card.dataset.search).includes(term);if(!card.hidden)count++;});document.querySelector('#archive-count').textContent=count+' publicaciones';});
