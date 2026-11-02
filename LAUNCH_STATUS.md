# Zawatu launch status

Updated 2 November 2026.

- GitHub Pages is enabled with GitHub Actions.
- The initial build and deployment succeeded.
- The owner saved `zawatu.com` as the custom domain; GitHub reported a successful DNS check.
- This commit triggers a new build so configure-pages supplies the custom domain origin and empty base path. Existing project-URL assets used `/zawatu/`; the custom domain must use root paths.
- HTTPS is not yet confirmed: the owner’s Pages screen showed Enforce HTTPS unavailable. Inspect certificate and DNS status before declaring the HTTPS domain live.
- Preserve Hostinger mail records when changing web records.
- Calendly scheduling/payment and verified social URLs remain to be connected.
