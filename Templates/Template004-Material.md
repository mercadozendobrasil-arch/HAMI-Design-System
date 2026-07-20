# Template004 — Material

Version: 2.1.0
Status: LOCKED

## Purpose
Show verified material, texture, transparency and construction details using source-derived product pixels.

## Required inputs
- One valid Product Library record.
- One complete product asset.
- One or two real detail assets or traceable crops from that same asset.
- Verified material metadata.

Return `BLOCKED_UNVERIFIED_MATERIAL` when the material claim is not recorded.

## Canvas
- 800 × 800 px, RGB, PNG.
- Global silver background.
- Safe area 40 px; 8-point grid.

## Fixed composition
- Header: x 40–760, y 40–144.
- Main product: x 40–500, y 150–690.
- Detail card A: x 520–760, y 190–390.
- Detail card B: x 520–760, y 414–614.
- Footer/model line: x 40–760, y 716–760.
- Use one or two detail cards only.

## Components
Use only `Title`, `ProductCard`, `FeatureCard`, `Callout` and `Divider`.

## Typography
- Montserrat only.
- Title maximum two lines.
- Detail labels one line preferred, two maximum.
- No paragraph descriptions.

## Crop provenance
- Every crop must be traceable to the same product record, color and asset set.
- Crops may enlarge existing pixels but cannot reconstruct missing texture.
- Do not use generic material stock photos.
- Do not simulate layer thickness, hardness tests or laboratory results.

## Product integrity
Never alter transparency, texture, stitching, edge thickness, surface finish, cutouts, buttons, ports or proportions.

## Allowed claims
Only when supported:
- `TPU Flexível`
- `Acabamento em PU`
- `Traseira Transparente`
- `Toque Suave`
- `Material Resistente`

## Forbidden
- `Premium` as a material fact without evidence.
- Invented percentages, hardness values or thickness.
- Fake cross-sections or exploded layers.
- More than two material claims.
- Decorative macro imagery unrelated to the product.

## QA gate
Run:
1. ProductRecord-QA
2. MetadataClaim-QA
3. CropProvenance-QA
4. ProductLock-QA
5. Text-QA
6. Layout-QA
7. Final-QA

Reject if a crop cannot be traced, a material is inferred, more than two cards are used, text exceeds two lines or product pixels change.

## Output naming
`{style}-{model}-{color}-T04-material-800.png`

## Dependencies
Tokens, Title, ProductCard, FeatureCard, Callout, ProductLock, Prompt004 and QA modules.