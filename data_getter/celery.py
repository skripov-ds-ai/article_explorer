from __future__ import absolute_import
import time
import random
# from celery.app.control import Inspect
# from flask_celeryext import FlaskCeleryExt
from celery import Celery
from celery.schedules import crontab
from navigator import app
from datetime import timedelta
from data_getter.process_data import get_result, transaction_single_article
from data_getter.parse_categories import categories_to_long_name


def make_celery(app):
    celery_app = Celery(
        "getter",
        backend=app.config['CELERY_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery_app.conf.update(app.config)
    TaskBase = celery_app.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


celery_app = make_celery(app)


@celery_app.task()
def load_data_task(start, max_results):
    data = []
    for cat in categories_to_long_name.keys():
        time.sleep(3.5 + random.random())
        # print(fill_template(cat, start, max_results))
        data1 = get_result(cat, start, max_results)
        data.extend(data1)

    for datum in data:
        transaction_single_article(datum)


celery_app.conf.beat_schedule = {
    'load_data_task1': {
        'task': 'data_getter.celery.load_data_task',
        'schedule': crontab(hour=10, minute=10),
        'args': (0, 100),
    },
}
celery_app.conf.timezone = 'UTC'
