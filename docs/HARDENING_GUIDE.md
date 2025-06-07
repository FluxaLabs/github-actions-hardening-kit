# Hardening Guide – GitHub Actions Security Kit

> **FluxOps** • v0.1.0 • Updated 2025-06-07

## 1. Why Harden?
* **90 % of public workflow examples use unpinned actions.**
* Secret-based cloud keys sit in repo history → breach risk.
* SBOM & provenance now required by many gov supply-chain standards (SLSA, EO 14028).

## 2. What This Kit Provides
| Layer | Feature | File |
|-------|---------|------|
| **Identity** | OIDC federation (no PAT) | All workflows |
| **Integrity** | SHA-pinned actions | `pin-actions.py` |
| **Vuln Scan** | Trivy on every build | `docker_publish.yml` |
| **SBOM** | CycloneDX JSON for each image | `docker_publish.yml` |
| **Provenance** | SLSA generator attestation | `docker_publish.yml` |

## 3. Quick Start
```bash
curl -Ls https://raw.githubusercontent.com/FluxOps/github-actions-hardening-kit/main/templates/build_test.yml \
  -o .github/workflows/build_test.yml
