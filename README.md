# Zawatu — Systems architecture and data platforms

Bilingual English/French website for the Zawatu engineering consulting practice.

## Positioning

Systems design, data engineering, software engineering and platform engineering support one coherent consulting offer. The starting engagement is a scoped Systems & Data Architecture Review. ZAF (Zawatu Architecture Framework) is presented as an evolving methodology, not a certification or established industry standard. AI work begins with data foundations and evaluation. Research initiatives are kept separate and no provisional name is published.

The existing logo, forest green, cream and lime identity are retained. Obsolete marketing routes contain noindex client-side redirects. New content is linked through the sitemap, canonical and language alternate metadata. The root sitemap includes both languages; the existing French sitemap remains available.

## Build and validation

Requires Python 3.12+ (standard library).

```sh
python3 scripts/build.py
python3 scripts/check_site.py
node --check assets/site.js
```

Output is `dist/`. GitHub Pages deploys it through `.github/workflows/pages.yml`. `SITE_BASE_PATH` supports a subdirectory; `SITE_URL` overrides the canonical origin.

The active generator is `scripts/architecture_site.py`. Older generators are retained as source history and are not run by the build.

## Enquiries

Contact forms prepare a mailto draft to `elvis@zawatu.com`. No enquiry is transmitted by the website, no payment is collected and no appointment is reserved. The visitor must send the email in their mail application. Backend enquiry handling, authenticated client services, and payments require a separate implementation and hosting decision.

Existing confirmed consultation terms remain on `/consultation/#booking-policy`. The previous growth consultation prices are retired from the current offer. Each new engagement requires written scope, deliverables, fees and terms.

## ZAF documentation edition

`/zaf/` and `/fr/zaf/` now introduce a 15-chapter public reference dossier rather than a nine-step card grid. Each chapter has numbered subsections, an in-page contents list, chapter navigation, decision tables and acceptance criteria. Ten native SVG figures per language document the conceptual city, capabilities, domains, target, data lineage, integration, trust boundaries, deployment, governance and transition. Their captions distinguish logical roles from proven infrastructure.

Content is maintained in `content/zaf_dossier.json`, rendered by `scripts/zaf_dossier.py`. `/zaf/documentation/complete/` provides continuous reading and browser-print styles; no PDF or page-perfect PDF export is claimed. The original worked-case URL remains a summary with a link to the dossier. All institutional findings and recommendations in the public example are fictional. Client blueprint content is not reproduced.
