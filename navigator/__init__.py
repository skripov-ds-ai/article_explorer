import logging
from flask import Flask
from config import Config, CELERY_BROKER_URL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_misaka import Misaka
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# admin = Admin(app, name='explorer', template_mode='bootstrap4')
# admin.add_view(ModelView(User, db.session))

md = Misaka(math=True, math_explicit=True)
md.init_app(app)

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.DEBUG)
app.logger.addHandler(s_handler)


from navigator import models, routes
