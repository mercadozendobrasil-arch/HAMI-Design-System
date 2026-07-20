# Template006 — Details

Version: 2.1.0
Status: LOCKED

## Purpose
Make real cutouts, buttons, straps, closures, holders and construction details easy to inspect.

## Required inputs
- One valid Product Library record.
- One full product asset.
- Two to four real detail assets or traceable crops from the same record.

Return `BLOCKED_MISSING_DETAIL_ASSETS` when fewer than two verified details exist.

## Canvas
- 800 × 800 px, RGB, PNG.
- Global silver background, 40 px safe area, 8-point grid.

## Fixed composition
- Header: x 40–760, y 40–144.
- Main product: x 40–470, y 150–690.
- Detail grid: x 490–760, y 166–650.
- Use 2, 3 or 4 equal Feature Cards only.
- Footer/model line: x 40–760, y 716–760.

## Components
Use only `Title`, `ProductCard`, `FeatureCard`, `Callout` and `Divider`.

## Typography
- Montserrat only.
- Title maximum two lines.
- One short label per detail.
- One line preferred; two maximum.

## Detail rules
- Every crop must identify a visible, useful purchasing detail.
- Crops must be traceable to the same style, model and color.
- Keep crop scale consistent across cards.
- Labels must describe what is visible, not an inferred benefit.

## Product integrity
Never create or reposition camera holes, speaker holes, charging ports, buttons, clasps, straps, pen slots, stitches or magnets.

## Allowed labels
Only when visible and accurate:
- `Recortes Precisos`
- `Botões Protegidos`
- `Cinta Reforçada`
- `Fecho Seguro`
- `Suporte para Caneta`
- `Acesso às Portas`

## Forbidden
- Generic stock macros.
- More than four detail cards.
- Repeating the same structure in multiple cards.
- Labels claiming precision when the relevant opening is not clearly visible.
- Invented accessories or internal components.

## QA gate
Run:
1. ProductRecord-QA
2. CropProvenance-QA
3. DetailAccuracy-QA
4. ProductLock-QA
5. Text-QA
6. Layout-QA
7. Final-QA

Reject if any crop lacks provenance, detail geometry differs from the full product, labels exceed two lines or fewer than two meaningful details are available.

## Output naming
`{style}-{model}-{color}-T06-details-800.png`

## Dependencies
Tokens, Title, ProductCard, FeatureCard, Callout, ProductLock, Prompt006 and QA modules.