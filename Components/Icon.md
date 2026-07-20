# Icon Component

## Purpose
Render an approved SVG from the single HAMI outline library.

## Usage / Inputs
`iconId`, `sizeToken`, optional `colorToken`.

## Slots
One SVG viewport; no embedded label.

## Tokens
`icon.*`, `color.text.primary`, `color.accent.primary`.

## QA
Reject unknown IDs, raster substitutes, filled icons, mixed stroke widths or arbitrary colors.

## Dependencies / Related / Version
`../Brand/IconSystem.md`, `../Assets/icons/`; used by Selling Point, Badge and templates. Version `2.0.0`.
