import os 

class Config:
    SECRET_KEY = '6b303869c00816089cfe22b007147d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    