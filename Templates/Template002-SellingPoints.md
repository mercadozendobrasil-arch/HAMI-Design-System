# Template002 — Selling Points

Version: 2.1.0
Status: LOCKED

## Purpose
Present the product's verified benefits in a mobile-first Shopee detail image without changing the real product.

## Required inputs
- One valid Product Library record.
- One approved main product asset.
- Two to four metadata-backed selling points.
- HAMI logo asset and approved outline icons.

If any required input is missing, return `BLOCKED_MISSING_REQUIRED_ASSET`.

## Canvas
- 800 × 800 px, RGB, PNG.
- Use the global silver background token.
- Safe area: 40 px on all sides.
- Use the 8-point grid only.

## Fixed composition
- Header zone: x 40–760, y 40–152.
- Product zone: x 300–760, y 150–700.
- Selling-point zone: x 40–292, y 190–650.
- Footer/model zone: x 40–760, y 716–760.
- Product visual coverage target: 58–68% because this is an information page.
- The product remains the dominant visual element.

## Components
Use only:
- `Title`
- `ProductCard`
- `SellingPoint`
- `Divider`
- optional `ModelBadge`

Do not create new card, icon, divider, arrow or badge styles.

## Typography
- Montserrat only.
- Title: H2 token, maximum two lines.
- Selling-point label: feature token, preferably one line; maximum two.
- Model line: caption token, one line.
- Never reduce text below the minimum mobile token. Remove copy instead.

## Selling-point rules
- Minimum 2, maximum 4.
- Each point contains one approved outline icon and one short label.
- One point must describe one benefit only.
- Order points by purchase relevance, not decoration.
- Use Brazilian Portuguese.
- Claims must be explicitly supported by metadata or visible construction.

## Product integrity
- Use source pixels from one Product Library record only.
- No redraw, generative replacement, geometry correction or invented device.
- Do not modify cutouts, buttons, ports, corners, texture, transparency, ratio or perspective.
- Callouts and icons must not cover functional structures.

## Allowed examples
Only when verified:
- `Rotação 360°`
- `Ajuste Universal`
- `Encaixe Seguro`
- `Proteção Reforçada`
- `Uso Horizontal e Vertical`

## Forbidden
- More than four benefits.
- Paragraphs, decorative copy or repeated claims.
- Mixed icon families.
- Unverified words such as `indestrutível`, `militar`, `100% seguro` or `à prova de tudo`.
- Reusing a selling point only to fill empty space.

## QA gate
Run, in order:
1. ProductRecord-QA
2. ProductLock-QA
3. Text-QA
4. Icon-QA
5. Layout-QA
6. Final-QA

Reject when:
- any text block exceeds two lines;
- product coverage is outside 58–68%;
- fewer than two or more than four points are used;
- an icon is not from the approved outline set;
- a claim cannot be traced to metadata;
- product pixels or geometry changed.

## Output naming
`{style}-{model}-{color}-T02-selling-points-800.png`

## Dependencies
Tokens, Title, ProductCard, SellingPoint, Divider, ProductLock, Prompt002 and QA modules.