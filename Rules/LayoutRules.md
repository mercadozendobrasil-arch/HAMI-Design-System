# Layout Rules

## Purpose

Guarantee deterministic placement across every SKU and AI renderer.

## Usage

Load `../Tokens/layout.tokens.json`, `component.tokens.json` and spacing tokens. Templates select named zones; components occupy slots inside those zones.

## Rules

- Align every coordinate and dimension to `layout.grid` unless a token explicitly says otherwise.
- Keep all essential content inside `layout.safe.margin` and outside `layout.outer.exclusion`.
- Keep Logo placement fixed through `layout.cover.logo`.
- Do not overlap copy with Product Card bounds.
- Do not crop key product structures to satisfy a layout.
- Use the declared layer order; annotations may sit above product pixels only when they do not hide a key structure.
- Product coverage must remain between `layout.product.coverage.min` and `.max`.
- Empty slots collapse by tokenized spacing; do not invent decorative filler.

## QA

Reject non-grid coordinates, out-of-safe-area content, changed Logo anchors, product/text overlap, wrong layer order or hardcoded values outside token files.

## Dependencies

`../Brand/GridSystem.md`, `../Tokens/`, `ProductLock.md`.

## Related modules

`../Components/`, `../Templates/`, `../QA/Layout-QA.md`.

## Version

`2.0.0`
