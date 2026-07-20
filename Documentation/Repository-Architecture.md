# Repository Architecture

## Purpose

Define the ownership boundary between the HAMI design system and product library.

## Ownership

| Repository | Owns | Must not own |
|---|---|---|
| HAMI-Design-System | Brand, tokens, components, layouts, templates, prompts, QA, examples | SKU product pixels or product-specific facts |
| HAMI-Product-Library | Product PNGs, product metadata, series notes | Brand values, layout values or duplicated template rules |

## Dependency direction

The design system reads product records through stable paths. Product records declare compatible design-system versions but do not copy design-system files.

## Version

`2.0.0-dev`
