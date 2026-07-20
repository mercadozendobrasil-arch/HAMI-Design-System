# Component Contract

## Purpose

Define the shared interface for all HAMI components.

## Required fields

Every component declares purpose, inputs, output slots, token dependencies, content limits, product-lock impact, QA assertions, related modules and version. Components never own absolute layout positions; templates place them.

## Rules

- Consume tokens by name.
- Accept verified content only.
- Never alter product pixels.
- Expose deterministic bounds for QA.
- Do not duplicate another component's responsibility.

## Version

`2.0.0`
