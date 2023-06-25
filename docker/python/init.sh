#!/bin/sh
set -e

echo "Migrate"
cd /var/www/app/hanov && python manage.py migrate

echo "Generate static files"
python manage.py collectstatic --noinput

echo "Start python and gunicorn"
python manage.py runserver 0.0.0.0:8000 & gunicorn --bind 0.0.0.0:7777 hanov.wsgi:application