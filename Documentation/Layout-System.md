# Layout System

## Purpose

Explain how renderers compose a HAMI image without redesigning it.

## Composition flow

1. Create the canvas from canvas and background tokens.
2. Select the template's named zones from layout tokens.
3. Place the real Product Card first and verify Product Lock.
4. Place Title and template-specific components in their slots.
5. Apply natural shadow, annotations and Logo in token layer order.
6. Emit a QA manifest containing resolved bounds and token names.

## Constraints

Templates own placement. Components own internal structure. Tokens own values. Product Library owns product pixels and facts. No layer may take ownership from another.

## Dependencies

`../Tokens/`, `../Components/`, `../Rules/LayoutRules.md`.

## Related modules

All templates and QA validators.

## Version

`2.0.0`
