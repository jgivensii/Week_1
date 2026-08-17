import json
from pathlib import Path
from pydantic import ValidationError
from RestockItem_api.model import RestockItem
from RestockItem_api.config import AppSetting


class RestockItemError(Exception):
     """ base exception for all errors in this module """

class ManifestNotFoundError(RestockItemError):
    """ raise when the restock manifest file does not exist """
    
class InvalidManifestFormatError(RestockItemError):
    """ raise when manifest data cannot be loaded in due to format issues """
    
def load_manifest(path: Path | None = None) -> tuple[list[RestockItem], list[dict[str,list[str]]]]:
      
      print(f"\n--- FUNCTION NAME: {load_manifest.__name__} ---")
      
      resolved_path = path if path is not None else AppSetting().data_path
      
      try: 
          raw_text = resolved_path.read_text(encoding="utf-8")
          
      except FileNotFoundError as e:
          raise ManifestNotFoundError(f"No manifest data at {resolved_path}") from e
      
      try:
          rows = json.loads(raw_text)
      
      except json.JSONDecodeError as e:
          raise InvalidManifestFormatError(f"Manifest data could not be loaded in from {resolved_path}") from e
      
      valid_rows: list[RestockItem] = []
      error_rows: list[dict[str, list[str]]] = []
      
      for row in rows:
          try:
              valid_rows.append(RestockItem.model_validate(row))
          except ValidationError as e:
              err_msgs = [f"{e['loc']}: {e['msg']}" for e in e.errors()]
              error_rows.append({"id": row.get("id", "<no id>"), "errors": err_msgs})
              
      return valid_rows, error_rows