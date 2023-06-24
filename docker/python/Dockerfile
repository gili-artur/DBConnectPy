FROM python:3.11-alpine3.18

# позволяет переопределить оболочку по умолчанию, используемую для формы оболочки команд
#SHELL ["/bin/bash", "-c"]

#Копируем содержимое папки (в которой находится Dockerfile) в корень папки контейнера
#ADD . .

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

#CMD ["python","-u","main.py"]
#CMD ["python /var/www/app/hanov/manage.py runserver --insecure"]
CMD [ "python", "hanov/manage.py", "runserver", "0.0.0.0:8000" ]

#RUN useradd -rms /bin/bash yt && chmod 777 /opt /run
#WORKDIR /dbcp
#RUN mkdir /dbcp/static && chown -R yt:yt /yt && chmod 755 /yt
#COPY --chown=yt:yt . .
#RUN pip install -r requirements.txt
#USER yt
#CMD ["gunicorn","-b","0.0.0.0:8001","soaqaz.wsgi:application"]

