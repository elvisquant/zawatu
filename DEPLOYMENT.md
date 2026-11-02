# Zawatu deployment checklist

Prepared for `zawatu.com`, confirmed by the owner. No GitHub account name, repository URL, DNS provider or public contact details have been assumed.

## Required access

- GitHub account with permission to create/write the selected repository and administer Pages.
- DNS access for zawatu.com at its authoritative DNS provider.
- Approved public business contact details and publisher identity.

Do not send passwords, access tokens or recovery codes in chat. Use connected services or perform authenticated setup in your own account.

## Preserve existing services

Record the current nameservers, A/AAAA/CNAME records, MX records, TXT records and any API/admin/staging subdomains. Determine whether mail or another service uses the root address. Do not replace nameservers or delete unrelated records. Preserve the old website or a recoverable copy before switching its address.

## GitHub Pages sequence

Create or select the repository, push source, enable Pages with GitHub Actions, and verify the generated Pages URL. Verify domain ownership using the exact TXT value shown by GitHub. Set `zawatu.com` in Pages settings before pointing DNS. The Actions workflow uses Pages metadata for correct canonical URLs and asset paths; re-run it after changing the custom domain.

For an apex domain, GitHub documents these A targets:

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | YOUR-VERIFIED-ACCOUNT.github.io |

Replace the final placeholder with the actual GitHub account or organization hostname after it is known. It must not include a repository path. These records have not been applied. Check for conflicting existing apex AAAA records as well as A records; do not indiscriminately delete DNS. IPv6 can be configured with GitHub’s documented AAAA targets when desired. No wildcard records are needed.

When using the included Actions workflow, a CNAME file is not required and is not what configures the custom domain; set it in Pages settings.

DNS and HTTPS can take time. Verify both `https://zawatu.com` and `https://www.zawatu.com`, including the expected redirect. Check at least one article, a service page, the mobile menu, search and the downloadable brief. Never report the custom domain live based solely on a successful source push.

## Rollback

Keep a copy of the previous DNS configuration and prior deployed source commit. Revert source through Git and redeploy for content errors. For a hosting switch failure, restore the verified previous web records. Preserve mail-related records. If Pages hosting is removed, remove or repoint associated DNS rather than leaving it dangling.

## Official references

- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

Reviewed 2 November 2026. Values are deployment preparation, not evidence of a live custom domain.
