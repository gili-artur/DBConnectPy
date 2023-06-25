# Project DBConnectPy

Тестовый проект на основе Django, отображающий в UI список клиентов из базы данных.
Также же есть рабочий API, и swagger по пути http://../swagger

## Quickstart

1. Проверить что питон установлен:


    python3 --version
    Python 3.x.x

Если питон не установлен:

    sudo apt install python3 -y
    sudo apt install python3-pip -y

2. Установить необходимые пакеты


    pip install -r requirements.txt


3. Мигации:


    cd hanov
    python manage.py makemigrations
    python manage.py migrate


4. Создать файл ".env", прописать Django SECRET_KEY и подключение к БД

5. Запуск приложения:


    python manage.py runserver 

__________________________

Docker-compose

1. Поднять весь проект командой make up


    make up


2. Нужно создать Django администратора. Сделать это можно 2 способами:


    make app

    or

    docker exec -ti dbcp_python sh

Далее ввести команду создания администратора:


    python manage.py createsuperuser

    >>Имя пользователя (leave blank to use 'root'): admin
    Адрес электронной почты: 
    Password: 
    Password (again): 
    Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.
    Введённый пароль слишком широко распространён.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.


3. Основная страница сайта: 
http://127.0.0.1:8081/
http://127.0.0.1:8081/admin/ - Админка
http://127.0.0.1:8081/api/ - API
http://127.0.0.1:8081/swagger/ - Swagger
