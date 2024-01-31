# Тестовое задание в компанию ООО СТАНДАРТ

## Выполнил Алексеев Лев

## Технологии:

Python 3.11, Django 4, Django Rest Framework 3.14, PostgreSQL.

## Описание тестового задания:
Проект позволяет создание и просмотр Заявок на оплату всем пользователям, ригестрацию, аутентификацию, просмотр страницы Реквизитов и поиск/сортировку/фильтрацию с помощью AJAX запросов для аутентифицированных пользователей, просмотр других таблиц администратору и персоналу.

## Установка:

1. Склонируйте репозиторий на локальную машину:
   
    ```bash
    $ git clone https://github.com/alekseevpy/test_assignment_STANDART.git
    ```

2. Cоздайте и активируйте виртуальное окржение, установите зависимости:
   
    ```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    $ pip install -r requirements.txt
    ```

3. Заполните файл .env и выполните миграции:
   
    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

4. Создайте суперпользователя:
   
    ```bash
    $ python manage.py createsuperuser
    ```

5. Заполните базу данных тестовыми данными:

    ```bash
    $ python seed_runner.py
    ```

6. Запустите локальный сервер:

    ```bash
    $ python manage.py runserver
    ```

Проект будет доступен по адресу: http://127.0.0.1:8000/
Админ-панель: http://127.0.0.1:8000/admin/
API-документация: http://127.0.0.1:8000/swagger/
