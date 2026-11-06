"""Chapter-based public ZAF reference dossier with native, accessible figures."""
import html,json,re,textwrap
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[1]/'content/zaf_dossier.json').read_text())
def e(x):return html.escape(str(x),quote=True)
def inline(x):return re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',e(x))

def figure(kind,lang,chapter):
 fr=lang=='fr'
 specs={
 'capabilities':('Capabilities and accountable outcomes','Capacités et résultats attribués',
 [('Request','Business owner'),('Approve','Delegated authority'),('Fulfil','Operations owner'),('Support platform','System owner'),('Reconcile','Finance owner'),('Review evidence','Control owner')],
 [('Demander','Responsable métier'),('Approuver','Autorité déléguée'),('Exécuter','Opérations'),('Support plateforme','Responsable système'),('Rapprocher','Finance'),('Examiner les preuves','Contrôle')],[(0,1),(1,2),(2,4),(4,5)],
 'One journey crosses several capabilities. Supporting platform responsibilities enable the journey; they do not absorb its business authority.',
 'Un parcours traverse plusieurs capacités. Le support plateforme permet le parcours sans absorber l’autorité métier.'),
 'domains':('Domains above shared capabilities','Domaines et capacités communes',
 [('Requests','Versions and transitions'),('Fulfilment','Execution facts'),('Finance','Definitions and reconciliation'),('Identity and access','Shared service contract'),('Delivery and integration','Shared service contract'),('Operations and telemetry','Shared service contract')],
 [('Demandes','Versions et transitions'),('Exécution','Faits opérationnels'),('Finance','Définitions et rapprochement'),('Identité et accès','Contrat commun'),('Livraison et intégration','Contrat commun'),('Opérations et télémétrie','Contrat commun')],[(0,3),(1,4),(2,5)],
 'Domain owners retain business meaning. Shared capabilities expose governed contracts. These are responsibility boundaries, not mandatory independent deployments.',
 'Les domaines conservent le sens métier. Les capacités communes ont des contrats gouvernés. Ces frontières ne prescrivent pas des déploiements indépendants.'),
 'target':('Logical target and authoritative state','Cible logique et état faisant autorité',
 [('Browser','Drafts and commands'),('Application API','Policy and version checks'),('PostgreSQL','State, audit and outbox'),('Notifications','Deferred delivery'),('Worker','Recoverable background work'),('Reporting','Versioned projections')],
 [('Navigateur','Brouillons et commandes'),('API applicative','Droits et versions'),('PostgreSQL','État, audit et outbox'),('Notifications','Livraison différée'),('Worker','Travail récupérable'),('Reporting','Projections versionnées')],[(0,1),(1,2),(2,4),(4,3),(4,5)],
 'The API commits authoritative state. A worker processes committed outbox work for notifications and reporting. Identity, attachments and recovery storage require additional controlled boundaries.',
 'L’API valide l’état de référence. Le worker traite le travail validé pour notifications et rapports. Identité, pièces et reprise nécessitent d’autres frontières contrôlées.'),
 'data':('Information authority and reporting lineage','Autorité des données et traçabilité du rapport',
 [('Request version','Request domain'),('Approval record','Delegated authority'),('Fulfilment record','Operations domain'),('Quality exceptions','Assigned steward'),('Reconciliation','Finance contract'),('Published report','Cut-off and revision')],
 [('Version de demande','Domaine demandes'),('Approbation','Autorité déléguée'),('Exécution','Domaine opérations'),('Exceptions qualité','Responsable attribué'),('Rapprochement','Contrat finance'),('Rapport publié','Période et révision')],[(0,1),(1,2),(2,4),(4,3),(4,5)],
 'Reporting combines authoritative facts through a defined contract. Exceptions remain visible; publication identifies source coverage, cut-off and revision.',
 'Le reporting combine des faits faisant autorité selon un contrat. Les exceptions restent visibles ; la publication indique couverture, période et révision.'),
 'integration':('Command, atomic commit and deferred effects','Commande, validation atomique et effets différés',
 [('Command','Actor, key, version'),('Server validation','Authority and state'),('Atomic transaction','State, audit, outbox'),('Explicit rejection','No business mutation'),('Worker and consumers','Retries and deduplication'),('Recorded delivery','Outcome and exceptions')],
 [('Commande','Acteur, clé, version'),('Validation serveur','Autorité et état'),('Transaction atomique','État, audit, outbox'),('Refus explicite','Aucun changement métier'),('Worker et consommateurs','Reprises et doublons'),('Livraison enregistrée','Résultat et exceptions')],[(0,1),(1,2),(1,3),(2,4),(4,5)],
 'Invalid commands are rejected. Valid decisions commit before external delivery. Repeated delivery remains possible and requires idempotent handling.',
 'Les commandes invalides sont refusées. La décision valide précède la livraison externe. Des répétitions restent possibles et nécessitent un traitement idempotent.'),
 'trust':('Access and information trust boundaries','Frontières de confiance et accès',
 [('User boundary','Identity and scope'),('Application boundary','Business authorization'),('Data boundary','Least-privilege storage'),('Administrative access','Named and accountable'),('External destinations','Approved disclosure'),('Recovery copies','Protected and verified')],
 [('Utilisateurs','Identité et périmètre'),('Application','Autorisation métier'),('Données','Privilèges limités'),('Administration','Accès nominatif attribué'),('Destinations externes','Divulgation approuvée'),('Copies de reprise','Protection et vérification')],[(0,1),(1,2),(3,1),(1,4),(2,5)],
 'Every arrow crosses an access or information boundary requiring a policy, owner and evidence. Local hosting does not eliminate external disclosure paths.',
 'Chaque flèche traverse une frontière exigeant politique, responsable et preuve. L’hébergement local ne supprime pas les destinations externes.'),
 'deployment':('Conceptual deployment and recovery dependencies','Déploiement conceptuel et dépendances de reprise',
 [('Office access','Devices and connectivity'),('Application runtime','Approved infrastructure'),('Authoritative storage','Database and attachments'),('Release artifacts','Version and configuration'),('Monitoring and response','Signals and ownership'),('Protected recovery','Separate access and restore')],
 [('Accès antennes','Appareils et réseau'),('Exécution applicative','Infrastructure autorisée'),('Stockage de référence','Base et pièces'),('Artefacts de version','Version et configuration'),('Supervision et réponse','Signaux et responsables'),('Reprise protégée','Accès distinct et restauration')],[(0,1),(1,2),(3,1),(1,4),(2,5)],
 'Logical roles are shown without claiming independent physical failure domains or high availability. Host, power, network and recovery locations require a detailed deployment decision.',
 'Les rôles logiques ne prouvent ni domaines physiques indépendants ni haute disponibilité. Hôtes, alimentation, réseau et lieux de reprise restent à définir.'),
 'governance':('Architecture decision lifecycle','Cycle des décisions d’architecture',
 [('Propose','Context and evidence'),('Review','Affected owners'),('Accept or decline','Authorized decision'),('Implement','Named delivery owner'),('Verify','Acceptance evidence'),('Revisit','Trigger or changed context')],
 [('Proposer','Contexte et preuves'),('Examiner','Responsables affectés'),('Accepter ou refuser','Autorité habilitée'),('Réaliser','Responsable nommé'),('Vérifier','Preuves d’acceptation'),('Réexaminer','Déclencheur ou contexte')],[(0,1),(1,2),(2,3),(3,4),(4,5)],
 'An accepted decision retains its rationale and consequences. A review trigger starts a new assessment; it does not silently rewrite the earlier record.',
 'La décision conserve justification et conséquences. Un déclencheur ouvre une nouvelle revue sans réécrire silencieusement l’historique.'),
 'roadmap':('Delivery phases with evidence gates','Phases de transition et preuves de passage',
 [('Discover','Authority and definitions'),('Design','Boundaries and scenarios'),('Pilot','One office, one journey'),('Recover','Timed verified restore'),('Expand','Support and coverage'),('Review','Operating evidence')],
 [('Découvrir','Autorité et définitions'),('Concevoir','Frontières et scénarios'),('Piloter','Une antenne, un parcours'),('Restaurer','Exercice chronométré'),('Étendre','Support et couverture'),('Réviser','Preuves opérationnelles')],[(0,1),(1,2),(2,3),(3,4),(4,5)],
 'Progress is conditional on exit evidence. Durations and budgets are not implied by the diagram; scope and readiness determine the sequence.',
 'La progression dépend des preuves. Le dessin ne prescrit ni délais ni budget ; périmètre et préparation gouvernent le passage.')}
 if kind=='city':return city(lang,chapter)
 titleEN,titleFR,nodesEN,nodesFR,edges,descEN,descFR=specs[kind]
 title=titleFR if fr else titleEN;desc=descFR if fr else descEN;nodes=nodesFR if fr else nodesEN
 coords=[(25,70),(335,70),(645,70),(25,300),(335,300),(645,300)]
 uid=f'fig-{chapter}-{kind}'; arrows=''; shapes=''
 for a,b in edges:
  x,y=coords[a];xx,yy=coords[b]
  if y==yy:
   if xx>x:path=f'M{x+250} {y+55}H{xx-10}'
   else:path=f'M{x} {y+55}H{xx+260}'
  elif y<yy:path=f'M{x+125} {y+110}V{y+160}H{xx+125}V{yy-10}'
  else:path=f'M{x+125} {y}V{y-50}H{xx+125}V{yy+120}'
  arrows+=f'<path d="{path}"/>'
 for i,((x,y),(name,sub)) in enumerate(zip(coords,nodes)):
  rows=textwrap.wrap(name,width=23);txt=''.join(f'<tspan x="{x+17}" dy="{0 if j==0 else 23}">{e(line)}</tspan>' for j,line in enumerate(rows))
  shapes+=f'<g><rect class="dossier-node" x="{x}" y="{y}" width="250" height="110" rx="5"/><text class="dossier-node-title" x="{x+17}" y="{y+30}">{txt}</text><text class="dossier-node-sub" x="{x+17}" y="{y+93}">{e(sub)}</text></g>'
 svg=f'<svg viewBox="0 0 920 450" role="img" aria-labelledby="{uid}-title {uid}-desc"><title id="{uid}-title">{e(title)}</title><desc id="{uid}-desc">{e(desc)}</desc><defs><marker id="{uid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 10 5 0 10z" fill="currentColor"/></marker></defs><g fill="none" stroke="currentColor" stroke-width="2" marker-end="url(#{uid}-arrow)">{arrows}</g>{shapes}</svg>'
 return f'<figure class="dossier-figure"><div class="dossier-figure-label">Figure {chapter}.1 · {e(title)}</div><div class="dossier-graphic" tabindex="0" role="region" aria-label="{e(title)}">{svg}</div><figcaption>{e(desc)}</figcaption></figure>'

def city(lang,chapter):
 fr=lang=='fr';title='Une institution comme ville numérique' if fr else 'An institution as a digital city'
 desc=('Les bâtiments représentent des domaines autonomes. Les services communs, les voies d’intégration et la gouvernance leur permettent de coopérer. Illustration conceptuelle, sans déploiement implicite.' if fr else 'Buildings represent autonomous domains. Shared services, integration routes and governance let them cooperate. Conceptual illustration with no implied deployment.')
 labels=['Demandes','Opérations','Finance'] if fr else ['Requests','Operations','Finance'];buildings=''
 for i,(x,height) in enumerate([(90,160),(355,205),(620,175)]):
  y=300-height
  buildings+=f'<g><rect x="{x}" y="{y}" width="190" height="{height}" rx="3" fill="var(--paper)" stroke="currentColor" stroke-width="2"/><path d="M{x-12} {y}L{x+95} {y-45}L{x+202} {y}Z" fill="var(--lime)" stroke="currentColor" stroke-width="2"/>'
  for wx in range(3):
   for wy in range(2):buildings+=f'<rect x="{x+28+wx*53}" y="{y+28+wy*45}" width="27" height="26" fill="#cad2bd"/>'
  buildings+=f'<rect x="{x+78}" y="{300-48}" width="34" height="48" fill="var(--ink)"/><text x="{x+95}" y="328" text-anchor="middle" class="city-label">{labels[i]}</text></g>'
 people=''
 for x,y in [(300,342),(570,355),(50,345),(845,343)]:people+=f'<g stroke="currentColor" stroke-width="3" fill="var(--ink)"><circle cx="{x}" cy="{y-13}" r="6"/><path d="M{x} {y-5}v18m0-10-10 8m10-8 10 8m-10 2-8 15m8-15 8 15"/></g>'
 shared='Identité · intégration · livraison · observabilité' if fr else 'Identity · integration · delivery · observability';govern='Gouvernance : autorité, contrats et responsabilités' if fr else 'Governance: authority, contracts and responsibility'
 svg=f'<svg viewBox="0 0 920 500" role="img" aria-labelledby="city-title city-desc"><title id="city-title">{title}</title><desc id="city-desc">{desc}</desc><path d="M25 385H895" stroke="var(--ink)" stroke-width="34"/><path d="M25 385H895" stroke="var(--lime)" stroke-width="2" stroke-dasharray="13 15"/>{buildings}{people}<rect x="55" y="425" width="810" height="55" rx="6" fill="var(--ink)"/><text x="460" y="459" fill="var(--paper)" font-family="Arial,sans-serif" font-size="19" text-anchor="middle">{shared}</text><text x="460" y="30" class="city-label" text-anchor="middle">{govern}</text></svg>'
 return f'<figure class="dossier-figure"><div class="dossier-figure-label">Figure {chapter}.1 · {title}</div><div class="dossier-graphic" tabindex="0" role="region" aria-label="{title}">{svg}</div><figcaption>{desc}</figcaption></figure>'

def render_markdown(text,lang,chapter,anchor_prefix=''):
 lines=text.strip().splitlines();out=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('{{figure:'):
   out.append(figure(line[9:-2],lang,chapter));i+=1;continue
  if line.startswith('## '):
   title=line[3:];key=re.match(r'(\d+\.\d+)',title);ident=anchor_prefix+'section-'+(key.group(1).replace('.','-') if key else str(i))
   out.append(f'<h2 id="{ident}">{inline(title)}</h2>');i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    rows.append([x.strip() for x in lines[i].strip().strip('|').split('|')]);i+=1
   heads=rows.pop(0);caption='Tableau de décision' if lang=='fr' else 'Decision table'
   out.append('<div class="table-scroll" tabindex="0" role="region" aria-label="'+caption+'"><table><thead><tr>'+''.join('<th scope="col">'+inline(x)+'</th>' for x in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if j==0 else '<td>')+inline(x)+('</th>' if j==0 else '</td>') for j,x in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>');continue
  if line.startswith('- '):
   items=[]
   while i<len(lines) and lines[i].strip().startswith('- '):items.append(lines[i].strip()[2:]);i+=1
   out.append('<ul>'+''.join('<li>'+inline(x)+'</li>' for x in items)+'</ul>');continue
  paragraph=[]
  while i<len(lines) and lines[i].strip() and not lines[i].strip().startswith(('## ','|','- ','{{figure:')):paragraph.append(lines[i].strip());i+=1
  out.append('<p>'+inline(' '.join(paragraph))+'</p>')
 return ''.join(out)

def chapter_nav(lang,link,active=0):
 fr=lang=='fr'
 return '<aside class="dossier-sidebar"><nav class="dossier-toc" aria-label="'+('Chapitres ZAF' if fr else 'ZAF chapters')+'">'+link('zaf/reference-study/',('Sommaire du dossier' if fr else 'Dossier contents'),'dossier-home')+'<ol>'+''.join('<li>'+link('zaf/documentation/'+c['slug']+'/',f'<span>{c["number"]:02d}</span> {e(c[lang]["title"])}','is-current' if c['number']==active else '')+'</li>' for c in D['chapters'])+'</ol></nav></aside>'

def publish(lang,page,hero,section,link,cta):
 fr=lang=='fr';title='Zawatu Architecture Framework'
 intro=('Un dossier d’architecture organisé en chapitres : contexte, évaluation, preuves, conception, responsabilités et décisions exécutives.' if fr else 'A chapter-based architecture dossier: context, assessment, evidence, design, responsibility and executive decisions.')
 scope=('Étude de référence complémentaire · Édition publique de référence 1.0 · 5 novembre 2026 · Exemple institutionnel fictif. Aucun résultat client ou déploiement n’est revendiqué.' if fr else 'Supporting reference study · Public reference edition 1.0 · 5 November 2026 · Fictional institutional example. No client outcome or deployment is claimed.')
 reading=('<h2>Un document de travail pour décider et réaliser.</h2><p>Lire dans l’ordre pour suivre le raisonnement, ou ouvrir un chapitre selon la décision à préparer. Chaque chapitre contient analyse, recommandations, pièces attendues et conditions de validation.</p>' if fr else '<h2>A working document for decisions and delivery.</h2><p>Read in sequence to follow the reasoning, or open a chapter for the decision you need to prepare. Chapters contain analysis, recommendations, expected artifacts and acceptance conditions.</p>')
 index='<div class="dossier-introduction">'+reading+'<p class="method-note">'+scope+'</p><div class="dossier-actions">'+link('zaf/documentation/'+D['chapters'][0]['slug']+'/',('Commencer le chapitre 01 ↗' if fr else 'Start chapter 01 ↗'),'solid')+link('zaf/documentation/complete/',('Lecture continue / impression ↗' if fr else 'Continuous reading / print ↗'),'text-link')+'</div></div>'
 index+='<ol class="chapter-index">'
 for c in D['chapters']:
  subheads=re.findall(r'^## (.+)$',c[lang]['body'],re.M)
  desc=' · '.join(re.sub(r'^\d+\.\d+\s*','',x) for x in subheads[:3])
  index+='<li>'+link('zaf/documentation/'+c['slug']+'/',f'<span class="chapter-index-number">{c["number"]:02d}</span><span><h2>{e(c[lang]["title"])}</h2><p>{e(desc)}</p></span><span class="chapter-arrow" aria-hidden="true">↗</span>')+'</li>'
 index+='</ol>'
 page('zaf/reference-study/',title,intro,hero('ZAF / '+('DOSSIER D’ARCHITECTURE' if fr else 'ARCHITECTURE DOSSIER'),title,intro)+section(index,'dossier-index')+section('<h2>'+('Méthode et application' if fr else 'Method and application')+'</h2><p>'+('Le dossier documente la démarche. La synthèse du cas permet de suivre son application à un parcours précis. Les documents propres aux clients restent distincts de cette publication.' if fr else 'The dossier documents the method. The worked-case summary follows its application to one journey. Client-specific material remains separate from this public edition.')+'</p>'+link('zaf/case-study/',('Lire la synthèse du cas ↗' if fr else 'Read the worked-case summary ↗'),'text-link'),'soft'))
 all_content=[]
 for c in D['chapters']:
  n=c['number'];x=c[lang];subheads=re.findall(r'^## (.+)$',x['body'],re.M)
  contents='<details class="chapter-contents" open><summary>'+('Dans ce chapitre' if fr else 'In this chapter')+'</summary><ol>'+''.join('<li><a href="#section-'+re.match(r'(\d+\.\d+)',s).group(1).replace('.','-')+'">'+e(s)+'</a></li>' for s in subheads)+'</ol></details>'
  foot='<nav class="chapter-pagination" aria-label="'+('Navigation des chapitres' if fr else 'Chapter navigation')+'">'
  if n>1:foot+=link('zaf/documentation/'+D['chapters'][n-2]['slug']+'/',('← Chapitre précédent' if fr else '← Previous chapter'),'text-link')
  foot+=link('zaf/reference-study/',('Sommaire' if fr else 'Contents'),'text-link')
  if n<len(D['chapters']):foot+=link('zaf/documentation/'+D['chapters'][n]['slug']+'/',('Chapitre suivant →' if fr else 'Next chapter →'),'text-link')
  foot+='</nav>'
  body=hero(f'ZAF / '+('CHAPITRE' if fr else 'CHAPTER')+f' {n:02d} / 15',e(x['title']),scope).replace('page-hero wrap','page-hero wrap dossier-chapter-hero')
  body+='<div class="dossier-layout wrap">'+chapter_nav(lang,link,n)+'<article class="dossier-chapter">'+contents+render_markdown(x['body'],lang,n)+foot+'</article></div>'
  page('zaf/documentation/'+c['slug']+'/',x['title'],intro,body)
  all_content.append(f'<section class="print-chapter"><h2 class="print-chapter-title">{n:02d} · {e(x["title"])}</h2>'+render_markdown(x['body'],lang,n,'print-')+'</section>')
 printtitle='Dossier ZAF — lecture continue' if fr else 'ZAF dossier — continuous edition'
 printintro=('Utilisez la fonction Imprimer du navigateur pour enregistrer cette édition. Les tableaux et figures font partie du dossier ; vérifiez la mise en page selon votre format de papier.' if fr else 'Use your browser’s Print function to save this edition. Tables and figures are part of the dossier; review pagination for your selected paper size.')
 page('zaf/documentation/complete/',printtitle,intro,hero('ZAF / 1.0',printtitle,scope)+section('<p class="print-instructions">'+printintro+'</p>'+''.join(all_content),'continuous-dossier'))
