#!/bin/sh
set -e

echo 1
cd /var/www/app/hanov && python manage.py migrate

echo 2
python manage.py runserver 0.0.0.0:8000 & gunicorn --bind 0.0.0.0:7777 hanov.wsgi:application
