import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    PORT = str(os.environ.get("DB_PORT"))
    DIALECT = str(os.environ.get("DIALECT"))

    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET_KEY"))
    SQLALCHEMY_DATABASE_URI = 'postgres://'+USERNAME+ \
        ':'+PASSWORD+'@'+HOST+':'+PORT+'/'+DATABASE+''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
