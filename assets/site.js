const menu=document.querySelector('.menu-toggle'),nav=document.querySelector('#main-nav');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu){menu.setAttribute('aria-expanded','false');nav.classList.remove('open');}});
const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
document.querySelector('#article-search')?.addEventListener('input',event=>{const query=normalize(event.target.value);let count=0;document.querySelectorAll('[data-search]').forEach(card=>{card.hidden=!normalize(card.dataset.search).includes(query);if(!card.hidden)count++;});document.querySelector('#result-count').textContent=`${count} article${count===1?'':'s'}`;document.querySelector('#no-results').hidden=count!==0;});
// Enquiries remain drafts on the visitor's device until sent in their email app.
document.querySelectorAll('.consultation-inquiry').forEach(form=>form.addEventListener('submit',event=>{
 event.preventDefault();const data=new FormData(form),fr=document.documentElement.lang==='fr';
 const subject=fr?'Demande de conseil en architecture — Zawatu':'Architecture consulting enquiry — Zawatu';
 const fields=fr?[['Nom','name'],['Email','email'],['Organisation / projet','company'],['Domaine','area'],['Contexte et problème','details'],['Résultat et calendrier','outcome'],['Mission','engagement'],['Budget indicatif','budget']]:[['Name','name'],['Email','email'],['Organization / project','company'],['Area','area'],['Current environment and challenge','details'],['Outcome and timeline','outcome'],['Engagement','engagement'],['Indicative budget','budget']];
 const lines=[subject,...fields.map(([label,key])=>`${label}: ${data.get(key)|| (fr?'À discuter':'To be discussed')}`),fr?'Merci de confirmer le périmètre, les livrables, le calendrier, les honoraires et les conditions avant tout engagement.':'Please confirm scope, deliverables, timing, fees and terms before any engagement.'];
 form.querySelector('.inquiry-status').textContent=fr?'Brouillon préparé. Vérifiez et envoyez votre email dans votre messagerie. Aucune demande n’a été transmise par ce site.':'Draft prepared. Review and send it in your email app. This website has not submitted your enquiry.';
 window.location.href='mailto:'+form.dataset.email+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(lines.join('\n\n'));
}));
