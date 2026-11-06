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

## Eight-book ZAF library (0.2.0)

`/zaf/` is now the living library of eight books. `content/zaf_library.json` records the catalogue, statuses, stable section IDs and Book I / Section 01 draft. `scripts/zaf_library.py` renders the catalogue, book contents, first section, editorial governance and release history.

Book II preserves the founder-defined fifteen sections. Other outlines are explicitly proposed. Only Book I / Section 01 has drafted standards-library body text; no book is presented as accepted. Planned headings are not applicable rules. The previous fifteen-chapter illustrative dossier remains at `/zaf/reference-study/` with its original chapter URLs intact.

Publication is distinct from acceptance. Draft -> review -> accepted -> deprecated/withdrawn is an editorial process, not an automated approval system. External references are bibliographic pointers, with no claim of accreditation or clause-level conformance. Work proceeds one section and one book at a time.

### Book I / Section 02

Library 0.3.0 adds `ZAF-I-02` (Institutional Context & Stakeholder Concerns) as draft 0.1.0 in English and French. Bodies are stored under `draftSections` in `content/zaf_library.json`; the catalogue records each drafted section's slug. `scripts/zaf_context_figures.py` renders two accessible native SVG views. Register IDs are scoped to the document, and cross-section references require that prefix. Sections 01 and 02 remain drafts. The next planned section is 03.
