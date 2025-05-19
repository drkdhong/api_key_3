# app/config.py
import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(BASE_DIR, '..', '.env')
load_dotenv(dotenv_path)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    API_KEY = os.getenv('API_KEY')
