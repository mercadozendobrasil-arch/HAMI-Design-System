# Selling Point Component

## Purpose
Pair one verified benefit label with one approved outline icon.

## Inputs
`label`, `iconId`, optional `accent=false`.

## Slots
Icon then label, aligned on one baseline.

## Tokens
`font.feature`, `icon.*`, `icon.gap.label`, `color.text.primary`, `color.accent.primary`.

## QA
Reject labels over two lines, unknown icons, filled icon styles or unverified claims.

## Dependencies / Related / Version
`Icon.md`, `../Rules/TextRules.md`; used by `SellingPointList.md`. Version `2.0.0`.
