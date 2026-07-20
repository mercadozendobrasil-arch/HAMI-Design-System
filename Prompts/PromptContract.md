# Prompt Contract

## Required inputs
`productRecord`, `templateId`, `outputPath`; optional verified `copyOverrides`.

## Execution
Load `README.md` and `CODEX.md` in their required order, load the target product record, resolve the named template and dependencies, compose, emit a QA manifest, run required QA, and export only on pass.

## Failure behavior
Reject missing product assets, unverified claims, incompatible metadata, product-lock failure or QA failure. Never invent missing data.

Version `2.0.0`.
