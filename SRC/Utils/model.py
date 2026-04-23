from pydantic_settings import BaseSettings ,SettingsConfigDict
class Setting(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
    db_url:str
    app_pass:str
    api_key:str
    redis_url:str
setting=Setting()