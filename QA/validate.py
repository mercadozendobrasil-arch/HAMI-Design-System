#!/usr/bin/env python3
"""Deterministic HAMI manifest and PNG validator. Standard library only."""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path


SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")


def png_info(path: Path) -> tuple[int, int, int]:
    with path.open("rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            raise ValueError("output is not PNG")
        length = struct.unpack(">I", handle.read(4))[0]
        if handle.read(4) != b"IHDR" or length != 13:
            raise ValueError("invalid PNG IHDR")
        width, height, depth, color_type, _, _, _ = struct.unpack(">IIBBBBB", handle.read(13))
    if depth != 8 or color_type != 2:
        raise ValueError("PNG must be 8-bit RGB without indexed color or alpha")
    return width, height, color_type


def validate(manifest_path: Path) -> list[str]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    required = {
        "schemaVersion", "designSystemVersion", "productLibraryVersion", "template", "file",
        "fontFamily", "backgroundToken", "productCoverage", "logo", "textBlocks",
        "sellingPoints", "iconStyle", "sourceAssetSha256", "productLockPassed", "claimsVerified"
    }
    errors += [f"missing field: {key}" for key in sorted(required - data.keys())]
    if errors:
        return errors
    if data["schemaVersion"] != "1.0": errors.append("schemaVersion must be 1.0")
    if not re.fullmatch(r"Template00[1-9]", str(data["template"])): errors.append("invalid template")
    if data["fontFamily"] != "Montserrat": errors.append("fontFamily must be Montserrat")
    if data["backgroundToken"] != "background.default": errors.append("wrong background token")
    if data["iconStyle"] not in {"outline", "none"}: errors.append("iconStyle must be outline or none")
    if not 0.72 <= float(data["productCoverage"]) <= 0.75: errors.append("product coverage outside 72–75%")
    if len(data["sellingPoints"]) > 4: errors.append("more than four selling points")
    if any(len(str(block.get("text", "")).splitlines()) > 2 for block in data["textBlocks"]): errors.append("text block exceeds two lines")
    logo = data["logo"]
    if (logo.get("x"), logo.get("y")) != (40, 36) or not 105 <= logo.get("width", 0) <= 120: errors.append("wrong logo placement")
    if not SHA256.fullmatch(str(data["sourceAssetSha256"])): errors.append("invalid source asset SHA-256")
    if data["productLockPassed"] is not True: errors.append("product lock not approved")
    if data["claimsVerified"] is not True: errors.append("claims not verified")
    output = (manifest_path.parent / data["file"]).resolve()
    try:
        width, height, _ = png_info(output)
        if (width, height) != (800, 800): errors.append("canvas must be 800x800")
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    errors = validate(args.manifest)
    if errors:
        print("REJECT")
        for error in errors: print(f"- {error}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
