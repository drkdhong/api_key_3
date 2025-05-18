import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv   # .env 파일 로드
load_dotenv()

from main import create_app
app = create_app()
print(f"FLASK_APP: ")
print(f"FLASK_APP: {os.getenv('FLASK_APP')} ")
print(f"FLASK_ENV: {os.getenv('FLASK_ENV')} ")
print(f"FLASK_DEBUG: {os.getenv('FLASK_DEBUG')} ")
# /config/base.py 변수 LABELS 인쇄
from config.base import Config
print(Config.LABELS)   # ['1', '2', '3']
print(app.config['LABELS']) # ['1', '2', '3']

if __name__=="__main__":   # 
    app.run(debug=True)
