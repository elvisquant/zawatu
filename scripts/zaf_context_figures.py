"""Two institutional context views for ZAF-I-02, with textual alternatives."""
import html

def e(x):return html.escape(str(x),quote=True)
def figure(kind,lang):
 fr=lang=='fr';uid='zaf-i-02-'+kind
 if kind=='context':
  title='Institutional context and retained authority' if not fr else 'Contexte institutionnel et autorité conservée'
  desc=('The selected institution retains service, finance, operations and information ownership. Users exchange requests and outcomes; policy owners supply governing authority; providers supply bounded services and support. The dashed boundary denotes retained institutional authority, not staff employment or physical location. This is a reference view, not a confirmed real institution.' if not fr else 'L’institution conserve responsabilités de service, finance, opérations et information. Les utilisateurs échangent demandes et résultats ; les autorités fournissent les règles ; les fournisseurs assurent des services limités. La frontière indique l’autorité conservée, pas l’emploi ou la localisation des acteurs. Vue illustrative sans institution réelle confirmée.')
  inside=(['Service owner','Finance authority','Operations owner','Information owner'] if not fr else ['Responsable service','Autorité finance','Opérations','Propriétaire données'])
  outside=(['Users and representatives','Request / outcome','Policy and risk owners','Governing authority','External service provider','Bounded service','External support provider','Evidence / recovery'] if not fr else ['Usagers et représentants','Demande / résultat','Politique et risques','Autorité des règles','Fournisseur externe','Service délimité','Support externe','Preuves / reprise'])
  boundary='Selected institution · authority retained' if not fr else 'Institution étudiée · autorité conservée'
  shapes=f'<rect x="245" y="140" width="480" height="400" rx="8" fill="#e1e7d5" stroke="currentColor" stroke-width="2" stroke-dasharray="7 5"/><text x="485" y="175" text-anchor="middle" class="context-boundary">{boundary}</text>'
  for (x,y),label in zip([(270,220),(505,220),(270,390),(505,390)],inside):
   shapes+=f'<rect x="{x}" y="{y}" width="195" height="95" rx="5" class="dossier-node"/><text x="{x+97}" y="{y+52}" text-anchor="middle" class="context-name">{label}</text>'
  ext=[(15,260,205,100,outside[0],outside[1]),(260,20,450,80,outside[2],outside[3]),(750,240,220,100,outside[4],outside[5]),(750,410,220,100,outside[6],outside[7])]
  for x,y,w,h,name,sub in ext:
   shapes+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" class="dossier-node"/><text x="{x+w/2}" y="{y+34}" text-anchor="middle" class="context-name">{e(name)}</text><text x="{x+w/2}" y="{y+63}" text-anchor="middle" class="context-sub">{e(sub)}</text>'
  arrows='<path d="M220 310H237M485 100V132M725 290H742M725 460H742"/>'
  svgbody=shapes+'<g fill="none" stroke="currentColor" stroke-width="2" marker-end="url(#'+uid+'-arrow)">'+arrows+'</g>'
  size='0 0 990 580';caption='Figure 2.1'
 else:
  title='Concern-to-decision traceability' if not fr else 'Traçabilité de la préoccupation à la décision'
  desc=('A concern is linked to evidence or an explicit unknown, then to a proposed decision and an acceptance check. C-02 connects amended content to version-bound authority and a stale-approval rejection test. This is an illustrative chain, not completed verification.' if not fr else 'La préoccupation est reliée à une preuve ou inconnue, puis à une décision et un contrôle. C-02 relie contenu modifié, autorité versionnée et test de refus d’une version périmée. Chaîne illustrative, sans vérification achevée.')
  labels=(['C-02 · Concern','Approval differs from execution','Evidence or unknown','Trace the amended request','DEC-02 · Proposed decision','Approval bound to reviewed version','Acceptance scenario','Reject a stale approval'] if not fr else ['C-02 · Préoccupation','Approbation différente de l’exécution','Preuve ou inconnue','Suivre la demande modifiée','DEC-02 · Décision proposée','Approbation sur version examinée','Scénario d’acceptation','Refuser une version périmée'])
  shapes=''
  for i,(x,y) in enumerate([(25,30),(455,30),(455,230),(25,230)]):
   shapes+=f'<rect x="{x}" y="{y}" width="380" height="125" rx="5" class="dossier-node"/><text x="{x+20}" y="{y+40}" class="context-step-title">{e(labels[i*2])}</text><text x="{x+20}" y="{y+84}" class="context-sub">{e(labels[i*2+1])}</text>'
  arrows='<path d="M405 92H445M645 155V220M455 292H415"/>'
  svgbody=shapes+'<g fill="none" stroke="currentColor" stroke-width="2" marker-end="url(#'+uid+'-arrow)">'+arrows+'</g>'
  size='0 0 860 390';caption='Figure 2.2'
 svg=f'<svg viewBox="{size}" role="img" aria-labelledby="{uid}-title {uid}-desc"><title id="{uid}-title">{e(title)}</title><desc id="{uid}-desc">{e(desc)}</desc><defs><marker id="{uid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 10 5 0 10z" fill="currentColor"/></marker></defs>{svgbody}</svg>'
 return '<figure class="dossier-figure context-figure"><div class="dossier-figure-label">'+caption+' · '+e(title)+'</div><div class="dossier-graphic" tabindex="0" role="region" aria-label="'+e(title)+'">'+svg+'</div><figcaption>'+e(desc)+'</figcaption></figure>'
