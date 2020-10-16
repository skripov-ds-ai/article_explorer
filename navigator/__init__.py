from flask import Flask
from config import Config, CELERY_BROKER_URL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_misaka import Misaka


app = Flask(__name__)
app.config.from_object(Config)
app.config['CELERY_BROKER_URL'] = CELERY_BROKER_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)
md = Misaka(math=True, math_explicit=True)
md.init_app(app)


from navigator import models, routes
