import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'palladium')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'palladium')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5432)
    DB = os.environ.get('POSTGRES_DB', 'maindb')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = "fpao10asfaf84w678f38f2dsafas928"
    QLALCHEMY_TRACK_MODIFICATIONS = True