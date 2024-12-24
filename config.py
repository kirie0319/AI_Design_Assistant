import os
import sys
from dotenv import load_dotenv

# パスを追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    PHOTOSHOP_API_KEY = os.environ.get('PHOTOSHOP_API_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')