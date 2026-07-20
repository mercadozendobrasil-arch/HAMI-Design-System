#!/usr/bin/env python3
"""Validate the HAMI repositories using only the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree


DOC_FIELDS = ("Purpose", "Usage", "Dependencies", "Related", "Version")
TEMPLATE_FIELDS = (
    "Mission",
    "Canvas",
    "Layout",
    "Grid",
    "Typography",
    "Components",
    "Icons",
    "Spacing",
    "Product Rules",
    "Text Rules",
    "QA",
    "Examples",
)
DESIGN_DIRS = (
    "Brand",
    "Tokens",
    "Components",
    "Templates",
    "Rules",
    "Prompts",
    "QA",
    "Examples",
    "Assets",
    "Documentation",
)
PRODUCT_DIRS = (
    "Products/QT",
    "Products/T",
    "Products/TM",
    "Products/TC",
    "Products/JG360",
    "Products/MF",
    "Products/MS",
    "Products/XZ",
    "TabletCase",
    "GlassFilm",
    "SoftFilm",
    "Stylus",
    "Accessories",
    "Metadata",
    "Documentation",
)
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def validate_json(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {path}: {exc}")


def validate_svg(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*.svg"):
        try:
            ElementTree.parse(path)
        except (OSError, ElementTree.ParseError) as exc:
            errors.append(f"invalid SVG: {path}: {exc}")


def validate_docs(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        missing = [field for field in DOC_FIELDS if field not in text]
        if missing:
            errors.append(f"documentation contract missing {missing}: {path}")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            target = target.strip("<>")
            if not (path.parent / target).resolve().exists():
                errors.append(f"broken relative link: {path} -> {raw_target}")


def validate_templates(root: Path, errors: list[str]) -> None:
    templates = sorted((root / "Templates").glob("Template[0-9][0-9][0-9]-*.md"))
    expected = [f"Template{i:03d}" for i in range(1, 10)]
    actual = [path.name[:11] for path in templates]
    if actual != expected:
        errors.append(f"template set mismatch: expected {expected}, found {actual}")
    for path in templates:
        headings = set(re.findall(r"^##\s+(.+?)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE))
        missing = [field for field in TEMPLATE_FIELDS if field not in headings]
        if missing:
            errors.append(f"template sections missing {missing}: {path}")


def validate_paths(root: Path, required: tuple[str, ...], errors: list[str]) -> None:
    for relative in required:
        if not (root / relative).exists():
            errors.append(f"required path missing: {root / relative}")


def main(argv: list[str]) -> int:
    design_root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    product_root = Path(argv[2]).resolve() if len(argv) > 2 else None
    errors: list[str] = []

    validate_paths(design_root, DESIGN_DIRS, errors)
    validate_json(design_root, errors)
    validate_svg(design_root, errors)
    validate_docs(design_root, errors)
    validate_templates(design_root, errors)

    if product_root:
        validate_paths(product_root, PRODUCT_DIRS, errors)
        validate_json(product_root, errors)
        validate_docs(product_root, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Repository validation failed: {len(errors)} error(s).")
        return 1

    scope = "design system and product library" if product_root else "design system"
    print(f"Repository validation passed: {scope}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
