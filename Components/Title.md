# Title Component

## Purpose
Render one primary heading and optional subtitle.

## Usage / Inputs
`title`, optional `subtitle`, `alignment=left`, optional `accentSpan`.

## Slots
`title` and `subtitle`; empty subtitle collapses without reserved space.

## Tokens
`font.h1`, `font.subtitle`, `color.text.primary`, `color.text.secondary`, `title.maxLines`, `subtitle.maxLines`.

## QA
Reject overflow, more than two title lines, more than one subtitle line, or non-Montserrat output.

## Dependencies / Related / Version
`ComponentContract.md`, `../Rules/TextRules.md`; used by every template. Version `2.0.0`.
