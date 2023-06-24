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


    python manage.py runserver --insecure


