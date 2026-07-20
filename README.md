# Stockcentric Artifacts

Stable, versioned media used by Stockcentric's build-backed educational posts.

Every published file is immutable inside a versioned folder and listed in `manifest.json` with its SHA-256 hash and dimensions. The repository exists so scheduled posts can use direct, permanent HTTPS media URLs and so readers can inspect the same artifact that was reviewed.

## Validation

```bash
python -m stockcentric_artifacts.validate
python -m pytest -q
```

Assets are explanatory outputs, not investment recommendations. Investing-related artifacts state their data date, methodology, limitations, and reader-decision boundary on the artifact itself.

## Collections

- `ai-setup-doctor/v0.1.0`: four pages for the local setup-health tool.
- `technical-strategy-evidence-lab/v0.1.1`: four pages for the synthetic strategy-survival methodology receipt.
- `context-drift-ledger/v0.1.0`: four pages for the local handoff-freshness receipt.
