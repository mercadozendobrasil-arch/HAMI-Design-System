# Template003 — Stand

## Purpose
Provide the permanent HAMI stand specification.

## Usage
Select only for Stand intent, resolve every named dependency, then run the listed QA without changing layout.

## Mission
Explain verified stand positions or rotation without implying unsupported movement.
## Canvas
Use canvas, background and export tokens.
## Layout
One primary real pose and at most two auxiliary real poses in named auxiliary zones.
## Grid
Use global grid, safe area and product coverage tokens.
## Typography
Title and optional one-line subtitle using Montserrat roles.
## Components
Title, Product Card, Arrow and optional Badge.
## Icons
Outline direction/rotation icon only when motion is verified.
## Spacing
Use spacing tokens; arrows remain outside key product structures.
## Product Rules
Every pose must be a real Product Library asset; never reconstruct a stand or hinge.
## Text Rules
Brazilian Portuguese; angle values only from metadata; maximum two lines per block.
## QA
Run ProductLock-QA, Layout-QA and Final-QA; reject inferred angles or motion.
## Examples
`Uso Horizontal e Vertical` is allowed only when both source poses exist.
## Dependencies / Related / Version
Tokens, Arrow, Product Card, Product Lock and Prompt003. Version `2.0.0`.
