# Compatibility Card

## Purpose
Present a verified model group without third-party logos.

## Inputs
`heading`, `models[]`, optional `screenSize`, optional `yearRange`.

## Slots
Heading, up to five model rows and optional metadata row.

## Tokens
`font.h2`, `font.feature`, `card.padding`, `card.radius`, `border.hairline`, `shadow.card`.

## QA
Reject unverified models, more than five rows, text below caption size or overflow.

## Dependencies / Related / Version
`ProductCard.md`, `../Rules/TextRules.md`; used by Template008. Version `2.0.0`.
