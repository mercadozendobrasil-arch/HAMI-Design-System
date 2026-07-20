# Template007 — Colors

Version: 2.1.0
Status: LOCKED

## Purpose
Present verified, currently available colors of the same product structure without generative recoloring.

## Required inputs
- One valid Product Library record per color.
- At least two real color assets with matching geometry and view.
- Availability metadata and standardized Brazilian Portuguese color names.

If only one verified color exists, return `BLOCKED_INSUFFICIENT_COLOR_VARIANTS`.

## Canvas
- 800 × 800 px, RGB, PNG.
- Global silver background, 40 px safe area, 8-point grid.

## Fixed composition
- Header: x 40–760, y 40–136.
- Primary color product: x 190–690, y 130–590.
- Secondary color strip: x 40–760, y 600–710.
- Footer/model line: x 40–760, y 724–760.
- Show 2–6 colors total.
- Primary product uses the requested/default color; secondary products use equal-size thumbnails.

## Components
Use only `Title`, `ProductCard`, `ColorBadge` and `Divider`.

## Typography
- Montserrat only.
- Title maximum two lines.
- Color names one line each.
- Use exact color naming from metadata.

## Color integrity
- Every displayed color must use a real source image.
- No hue shift, recoloring, paint-over or AI-generated color variant.
- Compare only images with the same product structure, angle, crop and comparable lighting.
- Do not mix `Pink`, `Rosa` and `Rose`; preserve catalog naming.
- Normalize known spelling aliases only through metadata rules, for example `Lavanta` → `Lavanda` when approved.

## Layout rules
- Maintain one shared visual baseline.
- Equal thumbnail dimensions and gaps.
- Use color badges only as labels; do not use a swatch as proof of product color.
- Do not imply availability when stock metadata marks a color inactive.

## Forbidden
- Generic color dots without real product images.
- More than six variants.
- Mixing models or styles.
- Using different viewing angles that make colors look like different products.
- Decorative names not present in metadata.

## QA gate
Run:
1. ProductRecord-QA
2. VariantIdentity-QA
3. ColorSource-QA
4. Availability-QA
5. ProductLock-QA
6. Text-QA
7. Layout-QA
8. Final-QA

Reject if any color was generated, geometry differs, a variant is unavailable, names conflict with metadata or fewer than two verified colors exist.

## Output naming
`{style}-{model}-T07-colors-800.png`

## Dependencies
Tokens, Title, ProductCard, ColorBadge, ProductLock, Prompt007 and QA modules.