# QA System

## Purpose
Combine machine-verifiable image constraints with mandatory visual Product Lock review.

## Usage
Run `python QA/validate.py <manifest.json>` and the template-specific checklist before export. Any error rejects the image. Human checks remain mandatory for visual Product Lock evidence.

Repository release gate:

```powershell
python QA/validate_repository.py . ../HAMI-Product-Library
```

## Dependencies
`../Tokens/`, `../Rules/`, `../Templates/`.

## Related Modules
`Final-QA.md`, `image-manifest.schema.json`, `validate.py`, `validate_repository.py`.

## Version
`2.0.0`
