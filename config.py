import os
from dotenv import load_dotenv
# Tải biến môi trường từ file .env
load_dotenv()
class Config:
    GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
    SHEET_NAME = os.getenv("SHEET_NAME")
    IMAFOLDER_ID = os.getenv("IMAFOLDER_ID")
    CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH", "credentials.json")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    WORDPRESS_SITE_URL = os.getenv("WORDPRESS_SITE_URL")
    WORDPRESS_USERNAME = os.getenv("WORDPRESS_USERNAME")
    WORDPRESS_PASSWORD = os.getenv("WORDPRESS_PASSWORD")
    SITE_URL = os.getenv("SITE_URL")
