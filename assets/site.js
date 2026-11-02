const menu=document.querySelector('.menu-toggle');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));document.querySelector('#main-nav').classList.toggle('open',open);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu){menu.setAttribute('aria-expanded','false');document.querySelector('#main-nav').classList.remove('open');}});
let selectedCategory='all';
const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
function filterArticles(){const query=normalize(document.querySelector('#article-search')?.value||'');let count=0;document.querySelectorAll('[data-category]').forEach(a=>{const show=(selectedCategory==='all'||a.dataset.category===selectedCategory)&&normalize(a.dataset.search).includes(query);a.hidden=!show;if(show)count++;});const status=document.querySelector('#result-count');if(status)status.textContent=`${count} article${count===1?'':'s'}`;const empty=document.querySelector('#no-results');if(empty)empty.hidden=count!==0;}
document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{selectedCategory=b.dataset.filter;document.querySelectorAll('[data-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));filterArticles();}));
document.querySelector('#article-search')?.addEventListener('input',filterArticles);
document.querySelector('#brief-form')?.addEventListener('submit',e=>{e.preventDefault();const f=new FormData(e.target);const fields=[['Entreprise / projet','company'],['Nom','name'],['Objectif','objective'],['Budget indicatif','budget'],['Calendrier','timeline'],['Public et contexte','details']];const content='BRIEF DE PROJET — ZAWATU\n\n'+fields.map(([label,key])=>`${label} : ${f.get(key)||'Non précisé'}`).join('\n\n')+'\n\nDocument généré sur votre appareil. Aucune demande n’a été transmise à Zawatu.\n';const blobUrl=URL.createObjectURL(new Blob([content],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=blobUrl;a.download='brief-zawatu.txt';a.click();setTimeout(()=>URL.revokeObjectURL(blobUrl),1000);document.querySelector('#brief-status').textContent='Brief téléchargé. Aucun envoi n’a été effectué.';});
document.querySelector('.share-link')?.addEventListener('click',async()=>{const status=document.querySelector('.share-status');try{await navigator.clipboard.writeText(location.href);status.textContent='Lien copié.';}catch{status.textContent='Copiez le lien dans la barre d’adresse.';}});
const appointmentForm=document.querySelector('#appointment-form');
if(appointmentForm){
 const dateField=appointmentForm.querySelector('[name=date]');
 const now=new Date();dateField.min=[now.getFullYear(),String(now.getMonth()+1).padStart(2,'0'),String(now.getDate()).padStart(2,'0')].join('-');
 appointmentForm.querySelector('[name=timezone]').value=Intl.DateTimeFormat().resolvedOptions().timeZone||'';
 appointmentForm.addEventListener('submit',e=>{
  e.preventDefault();const data=new FormData(appointmentForm);
  const body=['CONSULTATION REQUEST — ZAWATU','Name: '+data.get('name'),'Email: '+data.get('email'),'Preferred date: '+data.get('date'),'Preferred time: '+data.get('time'),'Time zone: '+data.get('timezone'),'Objective: '+data.get('details'),'','This is a request. Availability, fee and terms require confirmation.'].join('\n\n');
  const address=appointmentForm.dataset.email;
  location.href='mailto:'+encodeURIComponent(address)+'?subject='+encodeURIComponent('Consultation request — Zawatu')+'&body='+encodeURIComponent(body);
  document.querySelector('#appointment-status').textContent='Email draft prepared. Review and send it in your email app; no appointment has been confirmed.';
 });
}
if(document.documentElement.lang==='en'){
 document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{const count=[...document.querySelectorAll('[data-category]')].filter(a=>!a.hidden).length;document.querySelector('#result-count').textContent=count+' article'+(count===1?'':'s');}));
 document.querySelector('#article-search')?.addEventListener('input',()=>{const count=[...document.querySelectorAll('[data-category]')].filter(a=>!a.hidden).length;document.querySelector('#result-count').textContent=count+' article'+(count===1?'':'s');});
}
