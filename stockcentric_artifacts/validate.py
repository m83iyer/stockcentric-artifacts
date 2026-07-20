"""Validate immutable public PNG artifacts against the checked-in manifest."""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


class ArtifactValidationError(RuntimeError):
    """A public artifact differs from its reviewed manifest."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != PNG_SIGNATURE or header[12:16] != b"IHDR":
        raise ArtifactValidationError(f"Not a valid PNG: {path}")
    return struct.unpack(">II", header[16:24])


def load_manifest(root: Path = ROOT) -> dict[str, Any]:
    value = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != 1:
        raise ArtifactValidationError("Artifact manifest is invalid")
    return value


def validate(root: Path = ROOT) -> list[dict[str, Any]]:
    manifest = load_manifest(root)
    entries = manifest.get("assets")
    if not isinstance(entries, list) or not entries:
        raise ArtifactValidationError("Artifact manifest has no assets")
    checked: list[dict[str, Any]] = []
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ArtifactValidationError("Artifact entry is invalid")
        relative = str(entry.get("path") or "")
        if not relative.startswith("artifacts/") or relative in seen:
            raise ArtifactValidationError(f"Artifact path is unsafe or duplicated: {relative}")
        path = (root / relative).resolve()
        try:
            path.relative_to(root.resolve())
        except ValueError as exc:
            raise ArtifactValidationError(f"Artifact escapes repository: {relative}") from exc
        if not path.is_file() or path.suffix.casefold() != ".png":
            raise ArtifactValidationError(f"Artifact file is missing: {relative}")
        digest = sha256_file(path)
        dimensions = png_dimensions(path)
        expected_dimensions = (int(entry.get("width", 0)), int(entry.get("height", 0)))
        if digest != entry.get("sha256"):
            raise ArtifactValidationError(f"Artifact hash changed: {relative}")
        if dimensions != expected_dimensions:
            raise ArtifactValidationError(f"Artifact dimensions changed: {relative}")
        seen.add(relative)
        checked.append({"path": relative, "sha256": digest, "width": dimensions[0], "height": dimensions[1]})
    return checked


def main() -> int:
    print(json.dumps({"status": "verified", "assets": validate()}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
