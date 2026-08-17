from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSetting(BaseSettings):
    model_config = SettingsConfigDict(env_file = ".env", env_prefix="RESTOCK_ITEM_API", extra ="ignore")
    
    data_path: Path = Path(Path(__file__).parent.parent / "data" / "restock_manifest.json")