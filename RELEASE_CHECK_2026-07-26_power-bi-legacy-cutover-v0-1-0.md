# Power BI Legacy Excel/CSV Cutover Receipt v0.1.0 media release

- Source artifact: `content/media/power-bi-legacy-cutover-receipt/page-1.png`
- Public path: `artifacts/power-bi-legacy-cutover-receipt/v0.1.0/page-1.png`
- SHA-256: `140d102f12d0994d5445e49017fe81922e9bf427647b237a7aad7634b52dd5e8`
- Dimensions: 1600 x 1600
- Design system: `stockcentric-artifact-v1`
- Artifact review: `operations/artifact_reviews/builder-20260726T154704Z-49690.json`
- Builder evidence: `free-tools/power-bi-legacy-cutover-receipt/proof/builder-20260726T154704Z-49690/release-evidence.json`

The independently approved v0.1.0 artifact evaluates six inert Power BI inventory records against Microsoft’s separate 31 July 2026 refresh-stop and 31 August 2026 load-stop boundaries for affected legacy Excel and CSV paths. It preserves current-path, unknown, pending-deadline and missing-migration-proof states and never treats an opening report as proof that its data is current.

The receipt performs no tenant, account, credential, report, refresh, Buffer, X or GitHub action. It cannot prove report equivalence, credential validity, gateway health, data accuracy, tenant authorization or successful migration. This append adds one immutable media file and one release receipt and updates only the manifest; no existing asset, implementation, test, workflow or security file is changed.
