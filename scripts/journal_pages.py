"""One publication with two distinct editorial tracks and truthful authorship."""
TRACKS={'business':('Business & Growth','business-growth/','Brands, media, sales and commercial relationships.'),'engineering':('Engineering & Systems','engineering-systems/','Data, software, architecture and the systems behind delivery.')}
def build(page,hero,a,u,e,articles,card):
    def listing(items):
      cats=sorted({x['category'] for x in items})
      buttons='<button data-filter="all" aria-pressed="true">All topics</button>'+''.join(f'<button data-filter="{e(c)}" aria-pressed="false">{e(c)}</button>' for c in cats)
      return f'<section class="section wrap"><div class="journal-tools"><div class="filters" role="group" aria-label="Filter by topic">{buttons}</div><label class="search-label">Search articles<input id="article-search" type="search" placeholder="Search a topic or question"></label></div><p id="result-count" class="fine" role="status">{len(items)} articles</p><div class="articles">'+''.join(card(x,i) for i,x in enumerate(items))+'</div><p id="no-results" hidden>No articles match. Try another topic or search.</p></section>'
    tracks='<section class="section wrap"><div class="track-grid">'+''.join(f'<a class="track-card" href="{u("blog/"+path)}"><span class="eyebrow">{name.upper()}</span><h2>{name}</h2><p>{desc}</p><span class="text-link">Explore the track ↗</span></a>' for name,path,desc in TRACKS.values())+'</div></section>'
    note='<section class="section wrap editorial-note"><span class="eyebrow">EDITORIAL APPROACH</span><p>Practical guides with clear bylines, illustrative examples and sources where useful. Zawatu Editorial identifies our organizational editorial content. Sponsored work will be labelled; illustrative examples are not client case studies.</p>'+a('feed.xml','Follow the journal via RSS ↗','text-link')+'</section>'
    page('blog/','The Zawatu Journal','Business growth and engineering perspectives, organized into two focused editorial tracks.',hero('THE ZAWATU JOURNAL','Ideas for business.<br><em>Thinking for systems.</em>','Two editorial tracks. Practical perspectives for people building businesses and the technology that supports them.')+tracks+listing(articles)+note,'blog')
    for key,(name,path,desc) in TRACKS.items():
      items=[x for x in articles if x.get('track','business')==key]
      page('blog/'+path,name+' — Journal',desc,hero('THE ZAWATU JOURNAL',name,desc)+'<div class="wrap journal-back">'+a('blog/','← All journal tracks','text-link')+'</div>'+listing(items)+note,'blog')
    for x in articles:
      key=x.get('track','business');name,path,_=TRACKS[key]
      cta='consulting/technical/' if key=='engineering' else 'consultation/'
      label='Discuss your engineering challenge ↗' if key=='engineering' else 'Explore a business consultation ↗'
      body=f'<article class="article-page wrap"><nav class="breadcrumb" aria-label="Breadcrumb">{a("blog/","Journal")} / {a("blog/"+path,name)}</nav><span class="eyebrow">{e(x["category"].upper())}</span><h1>{e(x["title"])}</h1><p class="byline">{e(x.get("author","Zawatu Editorial"))} · <time datetime="{e(x.get("published","2026-11-02"))}">2 November 2026</time> · Practical guide</p><div class="article-body">{x["body"]}</div><div class="article-end">{a(cta,label,"text-link")}<button class="share-link">Copy article link</button><span class="share-status" role="status"></span></div></article>'
      page('blog/'+x['slug']+'/',x['title'],x['title'],body,'blog',x)
