import json
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

from validate import validate


def chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def rgb_png(path: Path, width: int = 800, height: int = 800) -> None:
    raw = b"".join(b"\x00" + b"\xff\xff\xff" * width for _ in range(height))
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


class ValidateTests(unittest.TestCase):
    def manifest(self, root: Path) -> Path:
        rgb_png(root / "image.png")
        data = {
            "schemaVersion": "1.0", "designSystemVersion": "2.0.0", "productLibraryVersion": "1.0.0",
            "template": "Template001", "file": "image.png", "fontFamily": "Montserrat",
            "backgroundToken": "background.default", "productCoverage": 0.73,
            "logo": {"x": 40, "y": 36, "width": 112}, "textBlocks": [{"text": "Proteção\nCompleta"}],
            "sellingPoints": ["Encaixe Seguro"], "iconStyle": "outline", "sourceAssetSha256": "a" * 64,
            "productLockPassed": True, "claimsVerified": True
        }
        path = root / "manifest.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_valid_manifest_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(validate(self.manifest(Path(tmp))), [])

    def test_bad_font_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.manifest(Path(tmp)); data = json.loads(path.read_text()); data["fontFamily"] = "Arial"; path.write_text(json.dumps(data))
            self.assertIn("fontFamily must be Montserrat", validate(path))


if __name__ == "__main__":
    unittest.main()
