# GitHub Actions Security-Hardening Kit
Opinionated workflow templates with:
* **Pinned actions** (SHA, not `@v` tags)
* **OIDC** cloud auth — ditch long-lived secrets
* **SBOM + SLSA provenance** out of the box

## Quick Start
```bash
curl -sSfL https://raw.githubusercontent.com/FluxaLabs/github-actions-hardening-kit/main/templates/build_test.yml -o .github/workflows/build_test.yml
