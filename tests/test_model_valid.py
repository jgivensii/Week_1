from RestockItem_api.model import RestockItem


test_data =  {"sku": "SKU-1111", "warehouse": "west-3", "quantity": 33, "unit_cost": 10, "category": "electronics"}

def test_valid_model():
    valid_data = RestockItem.model_validate(test_data)
    assert "SKU-1111" == valid_data.sku
    assert "west-3" == valid_data.warehouse
    assert 33 == valid_data.quantity
    assert 10 == valid_data.unit_cost
    assert "electronics" == valid_data.category