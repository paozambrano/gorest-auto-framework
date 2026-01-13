import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN = os.getenv("GOREST_TOKEN")
    BASE_URL = os.getenv("BASE_URL")

    if not TOKEN:
        raise ValueError("ERROR: GOREST_TOKEN was not found in the .env file ")