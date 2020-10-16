from __future__ import absolute_import
# from celery.app.control import Inspect
# from flask_celeryext import FlaskCeleryExt
from celery import Celery
from celery.schedules import crontab
from navigator import app
from datetime import timedelta
from data_getter.process_data import *



# CELERY_TASK_LIST = [
#     'data_getter.process_database',
# ]
from config import CELERY_BROKER_URL
db_session = None


def make_celery(app):
    celery = Celery("getter", backend=app.config['CELERY_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)



    celery.Task = ContextTask
    return celery

app.config['CELERY_BACKEND'] = "redis://redis:6379/0"
app.config['CELERY_BROKER_URL'] = "redis://redis:6379/0"

# app.config['CELERYBEAT_SCHEDULE'] = {
# }
# app.config['CELERY_TIMEZONE'] = 'UTC'

celery = make_celery(app)




# celery_app = FlaskCeleryExt(app)
# celery_app = Celery(
#     app.import_name,
#     broker=app.config['CELERY_BROKER_URL'],
#     # include=CELERY_TASK_LIST
# )
# celery_app.conf.timezone = 'UTC'
# celery_app.conf.CELERY_REDIS_SCHEDULER_URL = app.config['CELERY_BROKER_URL']
# celery_app.conf.CELERY_REDIS_SCHEDULER_KEY_PREFIX = app.config['CELERY_BROKER_URL']
#
# # celery_app.config_from_object()
# celery_app.conf.update(app.config)
@celery.task()
def load_data_task():
    data = []
    for cat in [
        'math.CT'
        'stat.TH',
        'stat.ML',
        'math.QA',
        'math.MP',
        'eess.IV',
        'math.CA',
        'math.FA'
    ]:
        # print(fill_template(cat, 700, 100))
        data1 = get_result(cat, 5, 5)
        data.extend(data1)

    for datum in data:
        # logging.info(datum)
        transaction_single_article(datum)


celery.conf.beat_schedule = {
    'load_data_task1': {
        'task': 'data_getter.celery.load_data_task',
        'schedule': timedelta(minutes=5),
        # 'args': (),
    },
}
celery.conf.timezone = 'UTC'
# TaskBase = celery_app.Task
#
#
# class ContextTask(TaskBase):
#     abstract = True
#
#     def __call__(self, *args, **kwargs):
#         with app.app_context():
#             return TaskBase.__call__(self, *args, **kwargs)
#
#
# celery_app.Task = ContextTask
# celery_app.app = app

# celery.autodiscover_tasks()
# i = Inspect()
# print(10*"===", i.registered_tasks())
