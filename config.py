import os
basedir = os.path.abspath(os.path.dirname(__file__))


POSTGRES_USER = os.getenv('POSTGRES_USER', None)
POSTGRES_PW = os.getenv('POSTGRES_PW', None)
POSTGRES_URL = os.getenv('POSTGRES_URL', None)
POSTGRES_DB = os.getenv('POSTGRES_DB', None)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_shall_not_pass'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PW,
        url=POSTGRES_URL,
        db=POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

