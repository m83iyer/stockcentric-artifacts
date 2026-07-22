# Investing brief media release check

- Base commit: `72f52edd9cb9a460ff8d837d5ce7c8c541f0cf89`
- New immutable assets: eight
- Technical carousel: ITC, Sun Pharma, Apple and Exxon
- Fundamental carousel: Reliance, HDFC Bank, Apple and Exxon
- Market coverage: two India and two US outputs in each carousel
- Source proof: `strategy/PROOF_FIRST_INVESTING_SEQUENCE_2026-07-23.md`
- Gold-pass proof: `outputs/dual-market-analysis-goldpass/2026-07-22/goldpass-report.json`
- Existing versioned assets remain byte-identical.
- The sole test maintenance replaces a fixed twelve-square-asset assertion with manifest-count equality, a twelve-asset minimum, and the approved 1600x1600 or 1600x2000 dimensions.
- No implementation code or GitHub workflow changed.
