#!/bin/sh

sleep 10

/venv/bin/python manage.py migrate

/venv/bin/gunicorn --bind :8000 --workers 2 project.wsgi