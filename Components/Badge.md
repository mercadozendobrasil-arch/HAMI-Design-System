# Badge Component

## Purpose
Display one short, verified status such as included quantity or compatibility grouping.

## Usage / Inputs
`label`, `tone=neutral|accent|success|warning`.

## Slots
Single-line label inside a pill container.

## Tokens
`radius.pill`, `font.caption`, `space.1`, semantic color tokens.

## QA
Reject promotional urgency, unsupported certification, more than one line or arbitrary colors.

## Dependencies / Related / Version
`ComponentContract.md`, `../Rules/TextRules.md`; used by Templates007–009. Version `2.0.0`.
