# Token Reference

## Purpose

Provide the complete reusable value layer for HAMI image generation.

## Usage

Load `index.json`, resolve every listed set, then resolve `{token.reference}` values. Components and templates must name tokens; they must not restate numeric or color values.

## Categories

Color, typography, spacing, radius, shadow, background, border, icon, animation and component tokens are all mandatory. Static exports use `motion.none`.

## Dependencies

`../Brand/` defines intent. Tokens are consumed by `../Components/`, `../Templates/`, `../Rules/` and `../QA/`.

## Version

`2.0.0`
