# PDF Table Extraction Fidelity Receipt v0.1.3 media release

- Source artifact: `content/media/pdf-table-extraction-fidelity-receipt/page-1.png`
- Public path: `artifacts/pdf-table-extraction-fidelity-receipt/v0.1.3/page-1.png`
- SHA-256: `f085c360638c4fd50710161a0da35e95e8a8d62cf940aae1fb3811facca37ce8`
- Dimensions: 1600 x 1600
- Design system: `stockcentric-artifact-v1`
- Artifact review: `operations/artifact_reviews/builder-20260725T021703Z-31165.json`
- Builder evidence: `free-tools/pdf-table-extraction-fidelity-receipt/proof/builder-20260725T021703Z-31165/release-evidence.json`

The independently approved v0.1.3 artifact compares six frozen machine-generated PDF fixtures against coordinate-labelled expected tables. It exposes extractor and version, table box, dimensions, header, value, duplicate and coordinate-level exception evidence, while refusing image-only scans. Its bounded renderer revision discovers the single Poppler PNG by deterministic prefix inside an isolated temporary directory and fails closed on zero or multiple outputs. It does not perform OCR, judge source truth, certify arbitrary PDFs, or use live, private or uploaded data. This append adds one immutable media file and one release receipt; no existing asset, implementation, test, workflow or security file is changed.
