from RestockItem_api.store import load_manifest

def test_valid_load_manifest():
    valid_output, invalid_output = load_manifest()
    assert len(valid_output)==8