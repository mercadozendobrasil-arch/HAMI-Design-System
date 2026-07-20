# Template003 — Stand Function

Version: 2.1.0
Status: LOCKED

## Purpose
Demonstrate verified stand positions, rotation or viewing modes using real product assets only.

## Required inputs
- One valid Product Library record.
- One primary real stand-position asset.
- Optional second and third real position assets.
- Verified angle or orientation metadata when numeric values are shown.

Missing real pose assets must return `BLOCKED_MISSING_REAL_POSE`.

## Canvas
- 800 × 800 px, RGB, PNG.
- Global silver background and 40 px safe area.
- 8-point grid.

## Fixed composition
- Header: x 40–760, y 40–144.
- Primary pose: x 250–760, y 140–690.
- Auxiliary pose A: x 40–250, y 210–410.
- Auxiliary pose B: x 40–250, y 430–630.
- Footer/model line: x 40–760, y 716–760.
- Primary pose must be visually dominant.
- Maximum three poses total.

## Components
Use only `Title`, `ProductCard`, `Arrow`, `Badge` and `Divider`.

## Typography
- Montserrat only.
- Title maximum two lines.
- Orientation labels one line preferred, two maximum.
- Numeric angles may be used only when metadata records the same value.

## Motion representation
- Arrows explain relationships; they must not imply movement unsupported by the product.
- Use rotation arrows only when rotation is verified.
- Keep arrows outside hinges, clasps, ports, buttons and corner attachments.
- Do not use animated, exploded or reconstructed mechanisms.

## Product integrity
- Every pose must originate from the same product record and color.
- Never synthesize a missing pose from another image.
- Never change stand angle, hinge geometry, buckle direction, device ratio or product thickness.
- A tablet/device shown inside the case must remain consistent across poses.

## Allowed labels
Only when verified:
- `Uso Horizontal e Vertical`
- `Ângulo Ajustável`
- `Rotação 360°`
- `Posição para Assistir`
- `Posição para Digitar`

## Forbidden
- More than three poses.
- Invented angle numbers.
- Fake motion blur or dramatic action effects.
- Showing a position the real product cannot hold.
- Long usage descriptions.

## QA gate
Run:
1. ProductRecord-QA
2. PoseProvenance-QA
3. ProductLock-QA
4. MotionClaim-QA
5. Text-QA
6. Layout-QA
7. Final-QA

Reject if any pose lacks a source asset, perspective is reconstructed, an angle is inferred, text exceeds two lines or arrows cover functional structures.

## Output naming
`{style}-{model}-{color}-T03-stand-800.png`

## Dependencies
Tokens, Title, ProductCard, Arrow, Badge, ProductLock, Prompt003 and QA modules.