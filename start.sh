#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi -b 0.0.0.0:8000 -w 4 --reload