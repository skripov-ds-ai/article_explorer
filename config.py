import os
basedir = os.path.abspath(os.path.dirname(__file__))



POSTGRES_USER = 'navigator'
POSTGRES_PW = 'qwerty2'
POSTGRES_URL = "127.0.0.1:5432"
POSTGRES_DB = "explorer"


# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
#         user=POSTGRES_USER,
#         pw=POSTGRES_PW,
#         url=POSTGRES_URL,
#         db=POSTGRES_DB
# )

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_shall_not_pass'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PW,
        url=POSTGRES_URL,
        db=POSTGRES_DB
    )
    #os.environ.get('DATABASE_URL')# or \
                              # 'sqlite:///' + os.path.join(basedir, 'explorer.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

