# Zawatu — static agency website and journal

French-language, responsive, multi-page website. No Node dependencies, tracking scripts, CMS, contact backend or paid features. Python 3 builds ordinary HTML/CSS/JavaScript that can run on GitHub Pages or a static web server.

## Edit and build

- Public details and domain: `content/site.json`. Empty contact fields are intentionally not invented.
- Journal articles: `content/articles.json`. Article bodies contain trusted editorial HTML; do not put untrusted submissions in this file.
- Pages and navigation: `scripts/build.py`.
- Design and interactions: `assets/site.css` and `assets/site.js`.

```bash
python3 scripts/build.py
python3 scripts/check_site.py
python3 -m http.server 8000 --directory dist
```

To preview a GitHub project path, set both `SITE_BASE_PATH=/repository-name` and `SITE_URL=https://YOUR-ACCOUNT.github.io` when building and the same `SITE_BASE_PATH` when checking. Production custom-domain builds use an empty base path. The Actions workflow obtains these settings from GitHub Pages.

## GitHub publication

1. Use a new repository, for example `zawatu-website`; do not overwrite an existing project.
2. Push this source to `main`.
3. In Settings → Pages choose GitHub Actions as the source.
4. Run or re-run the included workflow, and verify the deployment succeeds.
5. Verify domain ownership in your GitHub account, then set `zawatu.com` in the repository’s Pages settings **before changing DNS**.
6. Apply the records in `DEPLOYMENT.md` after checking existing DNS, including any existing website and mail dependencies.
7. Wait for the DNS check and certificate, then enable Enforce HTTPS.

If Pages is not yet enabled when the first workflow runs, enable it and re-run the workflow. Do not weaken mandatory checks to make deployment pass.

GitHub Pages has restrictions on online businesses and sites primarily facilitating commercial transactions. This release is an informational agency presentation and editorial publication, without checkout, SaaS or paid transactions. Review suitability against GitHub’s current terms before using it to operate additional commercial functions. GitHub can still store source if another host is selected.

## Contacts and public launch

Fill the verified email, international WhatsApp number, publisher identity and social URLs in `content/site.json`, then rebuild. The page currently downloads a local brief and clearly states that no enquiry is sent. An empty contact configuration does not create a working customer contact channel. No mailing list, sponsorship billing or advertising is active.

Before opening commercial enquiries: complete publisher information, approved public contact details and any locally applicable publishing requirements. Do not publish client references without permission. Campaign concepts are labelled illustrative.

## Moving to your server

Run the build and copy **the contents of `dist/`** to the web root. The same individual article URLs can be retained. Serve directory `index.html` files, use `404.html` for missing pages, and obtain TLS for the domain. Switch DNS only after checking the new host. Keep the GitHub repository as the source of truth. A future CMS or enquiry backend is a separate implementation; replacing the host alone does not make the site dynamic.

## Ownership and portability

All site assets here are local. No remote font or image requests are needed. The GitHub export excludes Sites hosting identity, internal Git metadata and private business-planning documents. No open-source licence is granted automatically; confirm publication/licensing choices with the owner.

## International redesign

English is the main edition; French is available at `/fr/`. English posts are in `content/articles_en.json`; French posts are in `content/articles_fr.json`. The build runs `scripts/build_fr.py` and `scripts/global_site.py`. The French edition retains its own styling in `assets/legacy.css`.

The consultation page currently prepares an email request. A preferred date is not a confirmed reservation. To activate the external scheduling button, set `booking_url` in `content/site.json` to the verified HTTPS Calendly event link and rebuild. Configure real paid event pricing and a supported merchant account in Calendly before claiming that payment is collected during booking. The site does not collect card data or make payment-status decisions.

Public email: hello@zawatu.com. Office: Bancobu Ikirezi, new building, 5th floor, Burundi. Social profile links are deliberately left empty until the owner provides actual URLs; filling the `socials` mapping activates matching footer links and icons.

GitHub repository: https://github.com/elvisquant/zawatu. DNS and Pages administration remain separate from uploading source. Preserve Hostinger MX, SPF, DKIM, DMARC and other mail records during website DNS changes.
