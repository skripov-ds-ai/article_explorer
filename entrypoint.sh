#!/usr/bin/env bash
#python manage.py db upgrade
flask db init
flask db migrate
flask db upgrade
#python manage.py db init
#python manage.py db migrate
#python manage.py db upgrade
gunicorn -b 0.0.0.0:5000 app:app
