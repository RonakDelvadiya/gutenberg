from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class VarSettings():
    DB_NAME: str = os.getenv("DB_NAME", "gutenberg_db")
    DB_USER: str = os.getenv("DB_USER", "admin")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "admin")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = str(os.getenv("DB_PORT", 5432))

var_settings = VarSettings()