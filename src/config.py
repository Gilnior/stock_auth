import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    title: str = "Stock Auth"
    description: str = "Stock tracker with jwt authentication"
    version: str = "1.0.0"
    database_url: str = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = "HS256"

settings: Settings = Settings()
