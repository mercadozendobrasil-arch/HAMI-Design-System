# Template001 — Cover

## Purpose
Provide the permanent HAMI cover specification.

## Usage
Select only for Cover intent, resolve every named dependency, then run the listed QA without changing layout.

## Mission
Create the official-store first image: identify the real product and its primary verified value within one second.

## Canvas
Use `canvas.*`, `background.default` and RGB PNG export tokens.

## Layout
Use `layout.cover.logo`, `layout.cover.textZone` and `layout.cover.productZone`; variant A is the default. Variant B adds one real detail; variant C adds only an actually included accessory.

## Grid
Use `layout.grid`, safe margin and outer exclusion tokens. Product coverage is `layout.product.coverage.min–max`.

## Typography
Title Component with `font.h1`; optional subtitle with `font.subtitle`; Montserrat only.

## Components
Logo, Title, Product Card and zero to four Selling Point components.

## Icons
Approved outline icons only; omit icons when they do not improve comprehension.

## Spacing
Use spacing tokens; adjacent information groups use at least `space.3`.

## Product Rules
Product Card uses a verified Product Library asset and SHA-256. Never redraw, deform, recolor or hide key structures.

## Text Rules
Brazilian Portuguese; title maximum two lines, subtitle one line, maximum four short selling points; all claims verified.

## QA
Run Cover-QA, ProductLock-QA, Layout-QA and Final-QA. Reject wrong Logo anchors, coverage, background, font or product integrity.

## Examples
`Generate QT Redmi Pad 2 Shopee Cover` resolves this template after a valid QT product record exists. Examples illustrate the spec and never override it.

## Dependencies / Related / Version
`../Tokens/`, `../Components/`, `../Rules/`; Prompt001 and QA. Version `2.0.0`.
