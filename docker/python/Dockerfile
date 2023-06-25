FROM python:3.11-alpine3.18

# set environment variables
# запрет питону создавать в котнейнере файлы с кешом
ENV PYTHONDONTWRITEBYTECODE 1
# запрет stdout, stdr внутри контейнера
#ENV PYTHONUNBUFFERED 1

#  Обновление + установка приложений (бибилотек) для работы с Postgresql
RUN apk update && apk add --update --no-cache \
    postgresql \
    postgresql-dev
RUN pip install --upgrade pip

RUN mkdir -p /var/www/app
WORKDIR /var/www/app
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /var/www/app

RUN chmod 755 ./docker/python/init.sh

ENTRYPOINT ./docker/python/init.sh


