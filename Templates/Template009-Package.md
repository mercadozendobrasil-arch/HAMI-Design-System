# Template009 — Package Contents

Version: 2.1.0
Status: LOCKED

## Purpose
Show exactly what the buyer receives, with verified quantities and no implied accessories.

## Required inputs
- One valid Product Library record.
- Non-empty `packageContents` metadata.
- One real asset for every visible included item.
- Verified quantity for every item.

Return `BLOCKED_MISSING_PACKAGE_CONTENTS` when any item, quantity or source asset is missing.

## Canvas
- 800 × 800 px, RGB, PNG.
- Global silver background, 40 px safe area, 8-point grid.

## Fixed composition
- Header: x 40–760, y 40–136.
- Primary included product: x 40–470, y 160–670.
- Included-items grid: x 490–760, y 180–640.
- Footer/model line: x 40–760, y 716–760.
- Display 1–5 item types.
- Largest/primary purchased item must remain visually dominant.

## Components
Use only `Title`, `ProductCard`, `PackageItem`, `QuantityBadge` and `Divider`.

## Typography
- Montserrat only.
- Title maximum two lines.
- Item label format: `{quantity} × {item}`.
- One line preferred, two maximum.

## Content rules
- Every visible item must appear in `packageContents` metadata.
- Use real source assets; do not generate styluses, films, cleaning kits, tablets, cables or packaging.
- Distinguish included products from demonstration devices.
- When a tablet is shown only to demonstrate fit, it must not appear on this page unless included.
- Quantity badges must match metadata exactly.

## Allowed examples
Only when confirmed:
- `1 × Capa`
- `1 × Película Flexível`
- `1 × Película de Vidro`
- `1 × Caneta Touch`
- `1 × Kit de Limpeza`

## Forbidden
- `Tablet não incluso` as a workaround for showing a tablet; omit the tablet instead.
- Decorative boxes or accessories not shipped.
- More than five item types.
- Generic package renders.
- Unverified bonuses, gifts or free items.

## QA gate
Run:
1. ProductRecord-QA
2. PackageSchema-QA
3. AssetPresence-QA
4. Quantity-QA
5. ProductLock-QA
6. Text-QA
7. Layout-QA
8. Final-QA

Reject if any visible item lacks metadata, quantity differs, an accessory is implied, text exceeds two lines or the main purchased item is not dominant.

## Output naming
`{style}-{model}-{color}-T09-package-800.png`

## Dependencies
Tokens, Title, ProductCard, PackageItem, QuantityBadge, metadata schema, ProductLock, Prompt009 and QA modules.