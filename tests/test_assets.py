from __future__ import annotations

import json
from pathlib import Path

import pytest

from stockcentric_artifacts.validate import ArtifactValidationError, ROOT, validate


def test_all_manifest_assets_are_intact() -> None:
    checked = validate()
    assert len(checked) == 8
    assert all(item["width"] == 1600 and item["height"] == 1600 for item in checked)


def test_changed_asset_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "artifacts/example/v1").mkdir(parents=True)
    (tmp_path / "artifacts/example/v1/page-1.png").write_bytes(b"not a png")
    (tmp_path / "manifest.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "assets": [
                    {
                        "path": "artifacts/example/v1/page-1.png",
                        "sha256": "0" * 64,
                        "width": 1600,
                        "height": 1600,
                    }
                ],
            }
        )
    )
    with pytest.raises(ArtifactValidationError):
        validate(tmp_path)


def test_manifest_contains_only_versioned_pngs() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text())
    for entry in manifest["assets"]:
        parts = Path(entry["path"]).parts
        assert parts[0] == "artifacts"
        assert parts[-2].startswith("v")
        assert parts[-1].endswith(".png")
