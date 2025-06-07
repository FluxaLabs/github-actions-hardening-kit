# GitHub Actions Security-Hardening Kit
Opinionated workflow templates with:
* **Pinned actions** (SHA, not `@v` tags)
* **OIDC** cloud auth — ditch long-lived secrets
* **SBOM + SLSA provenance** out of the box

## Quick Start
```bash
curl -sSfL https://raw.githubusercontent.com/FluxaLabs/github-actions-hardening-kit/main/templates/build_test.yml -o .github/workflows/build_test.yml


### Pin GitHub Actions to Commit SHAs

This repo includes a `scripts/pin-actions.py` tool that automatically scans your `.github/workflows` YAML files and replaces unpinned GitHub Actions (e.g., `actions/checkout@v4`) with their full commit SHA. Pinning actions to a specific SHA improves security and reproducibility by ensuring your workflows always use the exact same version of each action. Run this script to harden your workflows against upstream changes.