import pytest
from RestockItem_api.model import RestockItem
from RestockItem_api.store import ValidationError
test_data =  [{"sku": "SKU-1111", "warehouse": "west-3", "quantity": 33, "unit_cost": 10},
              {"sku": "SKU-0001", "warehouse": "south-2", "quantity": 5, "unit_cost": 0, "category": "apparel"},
              {"sku": "SKU-1001", "warehouse": "North-1", "quantity": 0, "unit_cost": 20, "category":  "furniture"}]

@pytest.mark.parametrize("invalid_row", test_data)
def test_invalid_model(invalid_row):
    with pytest.raises(ValidationError):
     RestockItem.model_validate(invalid_row)
    
        
    