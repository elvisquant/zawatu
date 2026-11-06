"""Original institutional outcome views for ZAF-I-03; hypotheses, not results."""
import html,re

def e(x):return html.escape(str(x),quote=True)
def figure(kind,lang):
 fr=lang=='fr';uid='zaf-i-03-'+kind
 def box(x,y,w,title,sub):
  return f'<rect x="{x}" y="{y}" width="{w}" height="105" rx="5" class="dossier-node"/><text x="{x+w/2}" y="{y+37}" text-anchor="middle" class="context-step-title">{e(title)}</text><text x="{x+w/2}" y="{y+73}" text-anchor="middle" class="context-sub">{e(sub)}</text>'
 if kind=='outcomes':
  title='Contribution model and its assumptions' if not fr else 'Modèle de contribution et hypothèses'
  desc=('Resources support activities and outputs. Outputs may contribute to user outcomes, which may contribute to wider institutional impact. Dashed arrows are unproven hypotheses. Accurate updates, usable language and available assistance must be tested; observations may lead to revising the intervention. No effect has been measured.' if not fr else 'Les ressources soutiennent activités et livrables. Les livrables peuvent contribuer aux résultats des usagers, puis à un impact institutionnel. Les flèches pointillées sont des hypothèses non prouvées. Exactitude, langage et assistance sont à tester ; les observations peuvent conduire à réviser l’intervention. Aucun effet n’a été mesuré.')
  labels=(['Resources','Owner time / capacity','Activities','Trace / clarify / prototype','Outputs','States / history / access','User outcomes','Understand / resume / reconcile','Wider contribution','Accountable institutional service'] if not fr else ['Ressources','Temps / capacité','Activités','Retracer / clarifier / prototyper','Livrables','États / historique / accès','Résultats des usagers','Comprendre / reprendre / rapprocher','Contribution élargie','Service institutionnel responsable'])
  shapes=box(20,25,250,*labels[:2])+box(315,25,320,*labels[2:4])+box(680,25,280,*labels[4:6])+box(390,240,570,*labels[6:8])+box(390,450,570,*labels[8:10])
  shapes+='<rect x="20" y="240" width="320" height="315" rx="5" fill="#e1e7d5" stroke="currentColor"/>'
  notes=(['Assumptions to test','Accurate state updates','Understandable language','Available assistance','Evidence may change','the intervention'] if not fr else ['Hypothèses à tester','États exacts et à jour','Langage compréhensible','Assistance disponible','Les preuves peuvent','modifier l’intervention'])
  for i,t in enumerate(notes):shapes+=f'<text x="40" y="{280+i*43}" class="'+('context-step-title' if i==0 else 'context-sub')+'">'+e(t)+'</text>'
  arrows='<path d="M270 77H305M635 77H670"/><path d="M820 130V230M675 345V440" stroke-dasharray="7 5"/>'
  size='0 0 980 585';caption='Figure 3.1'
 else:
  title='Service value includes interruption and correction' if not fr else 'La valeur inclut interruption et correction'
  desc=('A local draft can resume after interruption but is not institutionally accepted. Submission produces an acknowledged request for review. Review can require correction, record a rejection, or authorize fulfilment and reconciliation. Correction returns to review with a new version. This simplified service journey shows ownership questions, not deployed software or universal policy rules.' if not fr else 'Un brouillon local reprend après interruption sans être accepté par l’institution. Le dépôt donne une demande reçue pour revue. La revue peut demander correction, enregistrer un refus ou autoriser exécution et rapprochement. La correction retourne en revue avec une nouvelle version. Ce parcours simplifié expose des responsabilités, pas un logiciel déployé ni des règles universelles.')
  labels=(['Local draft','Not institutionally accepted','Interrupted','Resume draft / assisted route','Received request','Receipt and authoritative state','Review','Version-bound authority','Correction','New version for review','Rejected','Reason / authorized next route','Fulfil and reconcile','Execute the approved version'] if not fr else ['Brouillon local','Pas d’acceptation institutionnelle','Interruption','Reprise / voie assistée','Demande reçue','Réception et état faisant autorité','Revue','Autorité liée à la version','Correction','Nouvelle version à examiner','Refus','Motif / voie suivante autorisée','Exécuter et rapprocher','Exécuter la version approuvée'])
  shapes=box(20,25,420,*labels[:2])+box(550,25,410,*labels[2:4])+box(20,225,420,*labels[4:6])+box(20,425,420,*labels[6:8])+box(550,225,410,*labels[8:10])+box(550,425,410,*labels[10:12])+box(20,625,420,*labels[12:14])
  arrows='<path d="M440 60H540M550 100H450M230 130V215M230 330V415M440 455H540M440 495H495V355H755V340M550 260H500V380H410V415M230 530V615"/>'
  submit='Submit' if not fr else 'Déposer';approve='Approve' if not fr else 'Approuver'
  shapes+=f'<text x="250" y="180" class="context-sub">{submit}</text><text x="250" y="580" class="context-sub">{approve}</text>'
  size='0 0 980 760';caption='Figure 3.2'
 # Each edge gets its own arrowhead, including paths with several segments.
 arrows=re.sub(r'<path d="([^"]+)"([^>]*)/>',lambda m: ''.join('<path d="'+edge+'"'+m.group(2)+'/>' for edge in re.findall(r'M[^M]+',m.group(1))),arrows)
 svg=f'<svg viewBox="{size}" role="img" aria-labelledby="{uid}-title {uid}-desc"><title id="{uid}-title">{e(title)}</title><desc id="{uid}-desc">{e(desc)}</desc><defs><marker id="{uid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 10 5 0 10z" fill="currentColor"/></marker></defs>{shapes}<g fill="none" stroke="currentColor" stroke-width="2" marker-end="url(#{uid}-arrow)">{arrows}</g></svg>'
 return '<figure class="dossier-figure context-figure outcome-figure"><div class="dossier-figure-label">'+caption+' · '+e(title)+'</div><div class="dossier-graphic" tabindex="0" role="region" aria-label="'+e(title)+'">'+svg+'</div><figcaption>'+e(desc)+'</figcaption></figure>'
