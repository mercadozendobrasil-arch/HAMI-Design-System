# Template008 — Compatibility

## Purpose
Provide the permanent HAMI compatibility specification.

## Usage
Select only for Compatibility intent, resolve every named dependency, then run the listed QA without changing layout.

## Mission
Prevent incorrect purchases by presenting verified compatible models clearly.
## Canvas
Use canvas, background and export tokens.
## Layout
Title, one supporting product view and tokenized Compatibility Cards grouped by series.
## Grid
Use global grid and safe-area tokens; maintain global product coverage through the supporting product view.
## Typography
Title, card headings and model rows using Montserrat; never reduce below caption token.
## Components
Title, Product Card, Compatibility Card and Divider.
## Icons
No third-party logos; outline device icon optional.
## Spacing
Use card padding and group spacing tokens.
## Product Rules
Use the exact Product Library record associated with compatibility metadata.
## Text Rules
Brazilian Portuguese; exact model, year and size formats; up to five models per card.
## QA
Run Compatibility-QA, ProductLock-QA, Layout-QA and Final-QA; reject inferred models.
## Examples
Model names are copied verbatim from `compatibleModels`; empty data blocks export nothing.
## Dependencies / Related / Version
Tokens, Compatibility Card, metadata schema and Prompt008. Version `2.0.0`.
