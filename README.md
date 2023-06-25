# Project DBConnectPy

---

Тестовый проект использующий фреймворк Django, отображающий в UI список клиентов из базы данных.
Также же есть рабочий API и Swagger


## Quickstart 

---
1. Поменять значение переменных: `PATH_TO_PROJECT` и `PATH_TO_STATIC` в файл по пути: `docker/env/.env`

   - `PATH_TO_PROJECT` - путь, где лежит проект
   - `PATH_TO_STATIC` - путь, где лежит статика от проекта


2. При помощи инструмента Make запустить сборку контейнеров `make up` либо командой 
`docker compose -f ./docker/docker-compose.yml --env-file ./docker/env/.env up -d --build`
   
3. По пути http://localhost:8081 - доступен наш проект

---


4. Что-бы создать Django администратора нужно провалиться в контейнер "dbcp_python". Сделать это можно командой `make app` или :


    docker exec -ti dbcp_python sh

Далее перейти в каталог проекта Django:


      cd hanov

      >>/var/www/app/hanov/

Ввести команду создания администратора и заполнить необходимые параметры:


    python manage.py createsuperuser

    >>Имя пользователя (leave blank to use 'root'): 
    Адрес электронной почты: 
    Password: 
    Password (again): 
    Superuser created successfully.


5. Основная страница сайта: 
http://127.0.0.1:8081/

http://127.0.0.1:8081/admin/ - Админка

http://127.0.0.1:8081/api/ - API

http://127.0.0.1:8081/swagger/ - Swagger

Эти пути продублированы на основной странице в левом меню