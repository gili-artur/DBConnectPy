FROM nginx:stable-alpine

COPY ./docker/nginx/default.conf /etc/nginx/conf.d/default.conf

COPY ./hanov/main/static /var/www/app/hanov/main/static

#COPY /venv/lib/python3.8/site-packages/rest_framework/static/rest_framework/