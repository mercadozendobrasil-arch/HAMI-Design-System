# Template005 — Protection

Version: 2.1.0
Status: LOCKED

## Purpose
Explain real protective geometry and coverage without unsupported certification, test or absolute-safety claims.

## Required inputs
- One valid Product Library record.
- One full product asset.
- One or two real protective-detail assets or traceable crops.
- Metadata confirming the described structure.

Return `BLOCKED_UNSUPPORTED_PROTECTION_CLAIM` when evidence is missing.

## Canvas
- 800 × 800 px, RGB, PNG.
- Global silver background, 40 px safe area, 8-point grid.

## Fixed composition
- Header: x 40–760, y 40–144.
- Main product: x 170–730, y 150–690.
- Callout A: x 40–270, y 210–370.
- Callout B: x 40–270, y 410–570.
- Footer/model line: x 40–760, y 716–760.
- Maximum two protection callouts.

## Components
Use only `Title`, `ProductCard`, `FeatureCard`, `Callout`, `Arrow` and `Divider`.

## Typography
- Montserrat only.
- Title maximum two lines.
- Protection labels one line preferred, two maximum.
- Avoid technical values unless metadata records them.

## Evidence rules
- Show only real corners, raised lips, reinforced edges, coverage areas or cushioning visible in the source assets.
- Callout lines must terminate on the exact structure being described.
- Do not add fake impact waves, broken floors, drop scenes or certification shields.
- Do not imply protection for areas not physically covered.

## Product integrity
Never enlarge corners, thicken borders, deepen lips, add cushioning, alter material layers or change geometry to make protection look stronger.

## Allowed claims
Only when visually and/or metadata supported:
- `Cantos Protegidos`
- `Bordas Reforçadas`
- `Proteção Frontal e Traseira`
- `Maior Cobertura nas Laterais`
- `Ajuda a Reduzir Impactos`

## Forbidden claims
- `Indestrutível`
- `Proteção 100%`
- `Grau Militar` without authorized certification
- specific drop heights without test documentation
- water, dust or shock ratings not recorded in metadata

## QA gate
Run:
1. ProductRecord-QA
2. ProtectionEvidence-QA
3. Claim-QA
4. ProductLock-QA
5. Text-QA
6. Layout-QA
7. Final-QA

Reject if a callout does not point to real structure, the product was visually strengthened, an absolute claim is used, text exceeds two lines or more than two callouts are shown.

## Output naming
`{style}-{model}-{color}-T05-protection-800.png`

## Dependencies
Tokens, Title, ProductCard, FeatureCard, Callout, Arrow, ProductLock, Prompt005 and QA modules.