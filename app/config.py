import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SCRAPFLY_API_KEY = os.getenv("SCRAPFLY_API_KEY")

