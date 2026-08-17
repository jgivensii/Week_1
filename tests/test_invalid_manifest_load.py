from RestockItem_api.store import load_manifest


def test_invalid_load_manifest():
    g_output, invalid_output = load_manifest()
    assert len(invalid_output)==4