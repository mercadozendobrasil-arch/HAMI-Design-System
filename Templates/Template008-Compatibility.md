# Template008 — Compatibility

Version: 2.1.0
Status: LOCKED

## Purpose
Prevent incorrect purchases by showing only verified compatible models in a mobile-readable format.

## Required inputs
- One valid Product Library record.
- Non-empty `compatibleModels` metadata.
- Exact model names, screen sizes and years where applicable.

Return `BLOCKED_MISSING_COMPATIBILITY_DATA` when the compatibility list is absent or ambiguous.

## Canvas
- 800 × 800 px, RGB, PNG.
- Global silver background, 40 px safe area, 8-point grid.

## Fixed composition
- Header: x 40–760, y 40–136.
- Supporting product view: x 40–310, y 170–650.
- Compatibility area: x 330–760, y 160–690.
- Footer warning/model line: x 40–760, y 716–760.
- Use 1–3 Compatibility Cards.
- Maximum five model rows per card.

## Components
Use only `Title`, `ProductCard`, `CompatibilityCard`, `Divider` and optional `WarningBadge`.

## Typography
- Montserrat only.
- Title maximum two lines.
- Group heading one line.
- Model row one line whenever possible; maximum two.
- Never reduce below the minimum mobile caption token.

## Data rules
- Copy model names verbatim from metadata.
- Preserve `+`, generation, year, screen size and suffixes such as `FE`, `Plus`, `A16`, `M2` and `M3`.
- Group only by a metadata-defined family or compatibility set.
- Do not infer compatibility from similar dimensions or marketing names.
- Empty groups must not render.

## Brand rules
- Do not use Apple, Samsung, Xiaomi, Redmi or other third-party logos.
- Brand names may appear as plain text only when needed for model identification.
- Do not imply authorization, certification or official partnership.

## Known compatibility examples
Use only when the Product Library record explicitly confirms them:
- `Galaxy Tab A9 (8.7") / A11 (8.7")`
- `Galaxy Tab A9+ (11") / A11+ (11")`
- `Galaxy Tab S9 FE / S10 FE`
- `iPad 10 / 11 (A16)`
- `iPad Air 4 / 5 / M2 / M3 (11")`

## Forbidden
- Inferred models.
- More than 15 total model rows.
- Tiny text, dense paragraphs or comma walls.
- Combining products with different camera or button layouts unless metadata explicitly declares the same case.
- Third-party logos.

## QA gate
Run:
1. ProductRecord-QA
2. CompatibilitySchema-QA
3. ExactModelName-QA
4. Compatibility-QA
5. ProductLock-QA
6. Text-QA
7. Layout-QA
8. Final-QA

Reject if any model is inferred, a suffix/year/size is omitted, text becomes unreadable, a group exceeds five rows or metadata cannot be traced.

## Output naming
`{style}-{compatibility-set}-T08-compatibility-800.png`

## Dependencies
Tokens, Title, ProductCard, CompatibilityCard, metadata schema, ProductLock, Prompt008 and QA modules.