# Feature Card

## Purpose
Group one product detail, one label and optional supporting caption.

## Inputs
`imageCrop`, `label`, optional `caption`, optional `iconId`.

## Slots
Real product crop, label and optional caption.

## Tokens
`card.*`, `font.feature`, `font.caption`, `border.hairline`, `shadow.card`.

## QA
Reject generated detail pixels, unrelated crops, captions over two lines or inconsistent radii.

## Dependencies / Related / Version
`Callout.md`, `Icon.md`, `../Rules/ProductLock.md`; used by Templates004–006. Version `2.0.0`.
