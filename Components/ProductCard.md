# Product Card

## Purpose
Place real product pixels within deterministic bounds while preserving Product Lock.

## Inputs
`assetPath`, `assetSha256`, `fit=contain`, optional `shadowToken=shadow.product`, optional `rotation`.

## Slots
Product layer and optional natural shadow layer.

## Tokens
`layout.product.coverage.*`, `shadow.product`, canvas and safe-area tokens.

## QA
Reject missing hashes, non-uniform scaling, key-structure cropping, unsupported rotations or generated replacement pixels.

## Dependencies / Related / Version
`../Rules/ProductLock.md`, `../QA/ProductLock-QA.md`; used by all templates. Version `2.0.0`.
