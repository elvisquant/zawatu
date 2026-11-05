"""Evidence-led ZAF case study, profile and bilingual engineering journal."""
import html,json,math,re
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[1]/'content/practice.json').read_text())
def esc(value):return html.escape(str(value),quote=True)
def word_count(blocks):
 return sum(len(re.findall(r'\w+',str(b.get('text',''))+' '+' '.join(map(str,b.get('items',[])))+' '+str(b.get('rows',[])))) for b in blocks)
def diagram(kind,lang):
 fr=lang=='fr'
 if kind=='architecture':
  title='Frontières et flux proposés' if fr else 'Proposed boundaries and flows'
  labels=([('Navigateur','Brouillons non transmis'),('API applicative','Droits et versions'),('PostgreSQL','État · audit · outbox'),('Notifications','Effets différés'),('Worker','Reprises et dédoublonnage'),('Reporting','Projections et fraîcheur')] if fr else [('Browser','Unsent drafts'),('Application API','Permissions and versions'),('PostgreSQL','State · audit · outbox'),('Notifications','Asynchronous effects'),('Worker','Retries and deduplication'),('Reporting','Projections and freshness')])
  coords=[(20,90),(340,90),(660,90),(20,300),(340,300),(660,300)]
  arrows='<path d="M260 140H330M580 140H650M780 190V245H460V290M340 350H270M580 350H650"/>'
  desc=('Le navigateur transmet à l’API qui valide une transaction PostgreSQL. Le worker lit la boîte d’envoi et traite notifications et reporting. Schéma logique simplifié : identité, pièces jointes et sauvegardes sont hors du dessin.' if fr else 'The browser calls the API, which commits a PostgreSQL transaction. The worker reads the outbox and handles notifications and reporting. Simplified logical diagram; identity, attachments and backups are outside this drawing.')
 else:
  title='Décision et effets différés' if fr else 'Decision and asynchronous effects'
  labels=([('Commande','Acteur · clé · version'),('Contrôle serveur','Droits · état · version'),('Validation atomique','Décision · audit · outbox'),('Refus explicite','Aucun changement métier'),('Traitement différé','Reprises idempotentes')] if fr else [('Command','Actor · key · version'),('Server checks','Authority · state · version'),('Atomic commit','Decision · audit · outbox'),('Explicit rejection','No business state change'),('Asynchronous work','Idempotent retries')])
  coords=[(20,70),(340,70),(660,70),(340,290),(660,290)]
  arrows='<path d="M260 120H330M580 120H650M460 170V280M780 170V280"/>'
  desc=('Une commande valide est enregistrée atomiquement ; une commande non autorisée ou périmée est refusée. Les notifications sont traitées après validation et peuvent être reprises.' if fr else 'A valid command is committed atomically; an unauthorized or stale command is rejected. Notifications are processed after commit and may be retried.')
 boxes=''
 for i,((x,y),(name,sub)) in enumerate(zip(coords,labels)):
  boxes+=f'<g><rect x="{x}" y="{y}" width="240" height="100" rx="7" class="diagram-box"/><text x="{x+16}" y="{y+38}" class="diagram-name">{esc(name)}</text><text x="{x+16}" y="{y+68}" class="diagram-sub">{esc(sub)}</text></g>'
 return f'<figure class="zaf-diagram"><div class="diagram-scroll" tabindex="0" role="region" aria-label="{esc(title)}"><svg viewBox="0 0 920 430" role="img" aria-labelledby="{kind}-title {kind}-desc"><title id="{kind}-title">{esc(title)}</title><desc id="{kind}-desc">{esc(desc)}</desc><defs><marker id="{kind}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 10 5 0 10z" fill="currentColor"/></marker></defs><g fill="none" stroke="currentColor" stroke-width="2" marker-end="url(#{kind}-arrow)">{arrows}</g>{boxes}</svg></div><figcaption>{esc(desc)}</figcaption></figure>'
def blocks(items,lang):
 out=[]
 for b in items:
  kind=b['type']
  if kind=='p':out.append('<p>'+esc(b['text'])+'</p>')
  elif kind=='h2':out.append('<h2>'+esc(b['text'])+'</h2>')
  elif kind=='note':out.append('<aside class="method-note">'+esc(b['text'])+'</aside>')
  elif kind=='list':out.append('<ul>'+''.join('<li>'+esc(x)+'</li>' for x in b['items'])+'</ul>')
  elif kind=='code':out.append('<pre><code>'+esc(b['text'])+'</code></pre>')
  elif kind=='table':
   out.append('<div class="table-scroll" tabindex="0" role="region" aria-label="'+('Tableau de comparaison' if lang=='fr' else 'Comparison table')+'"><table><thead><tr>'+''.join('<th scope="col">'+esc(x)+'</th>' for x in b['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">'+esc(x)+'</th>') if i==0 else ('<td>'+esc(x)+'</td>') for i,x in enumerate(row))+'</tr>' for row in b['rows'])+'</tbody></table></div>')
  elif kind=='diagram':out.append(diagram(b['kind'],lang))
  elif kind=='links':out.append('<h2>'+('Références techniques' if lang=='fr' else 'Technical references')+'</h2><ul>'+''.join('<li><a href="'+esc(url)+'" rel="noopener noreferrer">'+esc(name)+'</a></li>' for name,url in b['items'])+'</ul>')
 return ''.join(out)
def case_teaser(lang,link):
 fr=lang=='fr';x=D['case'][lang]
 return '<div class="case-feature"><div><p class="eyebrow">ZAF / '+('ÉTUDE ILLUSTRATIVE' if fr else 'WORKED EXAMPLE')+'</p><h2>'+esc(x['title'])+'</h2><p>'+esc(x['summary'])+'</p>'+link('zaf/case-study/',('Examiner les décisions ↗' if fr else 'Examine the decisions ↗'),'solid')+'</div><aside><span class="case-number">01</span><h3>'+('Une décision explicable.' if fr else 'A decision you can explain.')+'</h3><p>'+('9 étapes · 2 schémas · 4 décisions d’architecture' if fr else '9 stages · 2 diagrams · 4 architecture decisions')+'</p><p class="fine">'+('Institution fictive. Hypothèses et preuves attendues clairement distinguées.' if fr else 'Fictional institution. Assumptions and required evidence are clearly distinguished.')+'</p></aside></div>'
def journal_cards(lang,link):
 fr=lang=='fr';out=[]
 for a in D['articles']:
  x=a[lang];minutes=max(1,math.ceil(word_count(x['blocks'])/200))
  out.append('<article class="article-card" data-category="'+esc(a['category'])+'" data-search="'+esc(x['title']+' '+a['category'])+'">'+link('blog/'+a['slug']+'/', '<div class="article-art tone-0"><span>'+('ÉTUDE TECHNIQUE' if fr else esc(a['cover']))+'</span><small>ZAWATU / ENGINEERING</small></div><p class="article-meta">'+esc(a['category'])+'</p><h3>'+esc(x['title'])+'</h3><p>'+esc(x['summary'])+'</p><p class="card-byline">Zawatu Editorial · 5 Nov 2026 · '+str(minutes)+' min</p><span class="read">'+('Lire l’analyse ↗' if fr else 'Read the analysis ↗')+'</span>')+'</article>')
 return '<div class="articles advanced-journal">'+''.join(out)+'</div>'
def profile_evidence(lang,link):
 fr=lang=='fr'
 timeline=([('2020','Mados Group','Ingénierie logicielle'),('2023','Africonsnet','Ingénierie logicielle et gestion de projet'),('Depuis déc. 2024','Smart Data Services / indépendant','Logiciels backend, données et livraison de plateformes')] if fr else [('2020','Mados Group','Software engineering'),('2023','Africonsnet','Software engineering and project management'),('Since Dec. 2024','Smart Data Services / freelance','Backend software, data and platform delivery')])
 rows=([('Processus métier','Conception de workflows et permissions','Définir l’autorité, les transitions et les cas d’échec.'),('Backend et données','API, PostgreSQL et intégrations','Relier règles métier, cohérence et reporting.'),('Plateformes','Conteneurs, CI/CD et infrastructure cloud','Relier livraison, accès, exploitation et reprise.')] if fr else [('Business workflows','Workflow and permission design','Define authority, valid transitions and failure cases.'),('Backend and data','APIs, PostgreSQL and integrations','Connect business rules, consistency and reporting.'),('Platforms','Containers, CI/CD and cloud infrastructure','Connect delivery, access, operations and recovery.')])
 intro=('Mon travail relie l’ingénierie logicielle, les données et l’exploitation des plateformes. L’objectif du conseil est de rendre les décisions techniques explicables : responsabilités claires, données traçables et procédures que l’équipe peut réellement appliquer.' if fr else 'My work connects software engineering, data and platform operations. The purpose of consulting is to make technical decisions explainable: clear responsibilities, traceable data and procedures the team can actually operate.')
 body='<div class="profile-evidence"><div class="profile-intro"><span class="eyebrow">'+('PARCOURS ET PRATIQUE' if fr else 'BACKGROUND & PRACTICE')+'</span><h2>'+('De la réalisation aux décisions d’architecture.' if fr else 'From implementation to architectural decisions.')+'</h2><p>'+intro+'</p></div><div class="career-timeline">'+''.join('<article><span class="eyebrow">'+esc(year)+'</span><h3>'+esc(org)+'</h3><p>'+esc(role)+'</p></article>' for year,org,role in timeline)+'</div>'
 body+='<h2>'+('Comment cette expérience sert une mission' if fr else 'How that experience informs an engagement')+'</h2>'+blocks([dict(type='table',headers=(['Domaine','Expérience mobilisée','Question d’architecture'] if fr else ['Area','Experience applied','Architecture question']),rows=rows)],lang)
 body+='<h2>'+('Éléments consultables' if fr else 'Inspectable work')+'</h2><div class="evidence-grid">'
 cards=([('Une démarche documentée','L’étude ZAF illustre l’évaluation, les choix et leurs limites. Ce n’est pas une référence client.','zaf/case-study/','Étude ZAF ↗'),('Un processus de livraison visible','Le dépôt public de ce site contient le générateur, les contrôles de liens et le workflow de déploiement. Il démontre ce périmètre précis.','https://github.com/elvisquant/zawatu','Voir le dépôt ↗'),('Une pratique d’analyse','Le journal présente des règles de cohérence, des contrats de reporting et des critères de préparation opérationnelle.','blog/','Lire le journal ↗')] if fr else [('A documented approach','The worked ZAF study demonstrates assessment, decisions and their limits. It is not a client reference.','zaf/case-study/','Read the ZAF study ↗'),('A visible delivery process','This website’s public repository contains its generator, link checks and deployment workflow. It demonstrates that specific scope.','https://github.com/elvisquant/zawatu','Inspect the repository ↗'),('Engineering analysis','The journal develops consistency rules, reporting contracts and operational readiness criteria.','blog/','Read the journal ↗')])
 for title,desc,url,label in cards:
  target=('<a class="text-link" href="'+esc(url)+'" rel="noopener noreferrer">'+label+'</a>') if url.startswith('https:') else link(url,label,'text-link')
  body+='<article><h3>'+title+'</h3><p>'+desc+'</p>'+target+'</article>'
 body+='</div><p class="fine">'+('Le parcours professionnel est présenté à partir des informations fournies par Elvis. Les ressources publiques montrent une méthode et le périmètre qu’elles documentent ; elles ne prouvent pas des résultats clients confidentiels. Les réalisations institutionnelles ne sont détaillées qu’avec autorisation de divulgation.' if fr else 'Professional history is based on information provided by Elvis. Public materials demonstrate the method and scope they document; they do not establish confidential client outcomes. Institution-specific work is discussed only where disclosure is authorized.')+'</p></div>'
 return body
def publish_deep_pages(lang,page,hero,section,link,cta):
 fr=lang=='fr';x=D['case'][lang]
 page('zaf/case-study/',x['title'],x['summary'],hero('ZAF / '+('ÉTUDE ILLUSTRATIVE' if fr else 'WORKED EXAMPLE'),esc(x['title']),esc(x['summary']))+section('<article class="case-study-body">'+blocks(x['blocks'],lang)+'</article>')+section('<h2>'+('Appliquer cette démarche à votre contexte' if fr else 'Apply this approach to your context')+'</h2><p>'+('La première mission examine un parcours, ses données et ses risques, puis fournit une cartographie et des recommandations priorisées. Le périmètre et les honoraires sont convenus avant le démarrage.' if fr else 'A starting engagement examines one workflow, its data and its risks, then produces a current-state map and prioritized recommendations. Scope and fees are agreed before work begins.')+'</p>'+link('contact/',('Discuter d’une revue ↗' if fr else 'Discuss an architecture review ↗'),'solid'),'soft'))
 for a in D['articles']:
  x=a[lang];minutes=max(1,math.ceil(word_count(x['blocks'])/200))
  body=hero('JOURNAL / '+a['category'],esc(x['title']),esc(x['summary']))
  body+=section('<p class="reading-meta">Zawatu Editorial · 5 Nov 2026 · '+str(minutes)+' min</p><article class="article-body longform">'+blocks(x['blocks'],lang)+'</article>')
  body+=section('<div class="article-next"><span class="eyebrow">'+('DE LA LECTURE À LA PRATIQUE' if fr else 'FROM ANALYSIS TO PRACTICE')+'</span><h2>'+('Voir ces décisions dans une architecture complète.' if fr else 'See these decisions in a complete architecture.')+'</h2>'+link('zaf/case-study/',('Explorer l’étude ZAF ↗' if fr else 'Explore the ZAF study ↗'),'text-link')+'<p>'+('Une revue peut appliquer ces questions à un périmètre concret de votre organisation.' if fr else 'An architecture review can apply these questions to a concrete part of your organization.')+'</p>'+link('contact/',('Présenter votre contexte ↗' if fr else 'Describe your context ↗'),'solid')+'</div>','soft')
  page('blog/'+a['slug']+'/',x['title'],x['summary'],body)
