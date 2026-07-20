# Stockcentric Artifacts v0.1.0 Release Check

- Purpose: permanent, direct public media URLs for Buffer-scheduled Stockcentric posts.
- Design system: `stockcentric-artifact-v1`.
- Asset inventory: eight PNGs from two independently built and reviewed artifact bundles.
- Dimensions: every PNG is 1600 × 1600.
- Integrity: every path, SHA-256 and dimension is locked in `manifest.json`.
- Privacy: repository contains public visuals and deterministic validation code only; no credentials, cookies, browser state, personal records or signed URLs.
- Stealth: protected project identities are absent.
- Tests: `PYTHONPATH=. python3 -m pytest -q -p no:rerunfailures` passed 3/3 on Python 3.14. The host-wide rerun plugin was disabled because this sandbox blocks its localhost status socket.
- Validation: `PYTHONPATH=. python3 -m stockcentric_artifacts.validate` verified all eight files.
- Git state: isolated `main` repository; generated Python/build files are ignored.
- Publication rule: existing versioned paths and bytes are immutable. Future assets must use a new artifact/version path and pass the same hash, review and guarded-release checks.

The first release contains AI Setup Doctor v0.1.0 and Technical Strategy Evidence Lab v0.1.1, four pages each. Technical Strategy Evidence Lab entered the release source only after `reviewer-20260719T145921Z-66781` approved the corrected bundle and rendered design.
