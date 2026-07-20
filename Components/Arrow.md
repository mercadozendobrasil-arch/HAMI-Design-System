# Arrow Component

## Purpose
Indicate a verified direction, angle or relationship.

## Inputs
`path`, `direction`, optional `label`, `accent=false`.

## Slots
One outline path, one arrowhead and optional short label.

## Tokens
`icon.strokeWidth`, `icon.lineCap`, `color.text.primary`, `color.accent.primary`.

## QA
Reject arrows that imply unsupported motion, exceed product-safe bounds or use filled/3D styling.

## Dependencies / Related / Version
`ComponentContract.md`, `../Rules/ProductLock.md`; used by Templates003–006. Version `2.0.0`.
