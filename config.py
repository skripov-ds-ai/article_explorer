import os
basedir = os.path.abspath(os.path.dirname(__file__))


POSTGRES_USER = os.getenv('POSTGRES_USER', None)
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', None)
POSTGRES_URL = os.getenv('POSTGRES_URL', None)
POSTGRES_DB = os.getenv('POSTGRES_DB', None)
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', None)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_shall_not_pass'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PASSWORD,
        url=POSTGRES_URL,
        db=POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BACKEND = CELERY_BROKER_URL
    CELERY_BROKER_URL = CELERY_BROKER_URL

