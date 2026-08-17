from pathlib import Path
import pytest
from RestockItem_api.store import ManifestNotFoundError, load_manifest

path: Path = Path("Path(__file__).parent.parent/data/fake_path/fake_manifest.json")

def test_invalid_file_path():
    with pytest.raises(ManifestNotFoundError):
     load_manifest(path)