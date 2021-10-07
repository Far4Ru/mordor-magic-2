## Django

> **Установка** <BR> `Python 3.8` Windows 7 <BR> `Python 3.9+` Windows 10

Создание виртуального окружения

    py -m venv mordor-magic-env

Активация виртуального окружения

    mordor-magic-env\Scripts\activate.bat

Установка Django в виртуальное окружение

    pip install django

Создание миграций на основе моделей

    python manage.py makemigrations

Применение миграций

    python manage.py migrate

Создание суперпользователя

    python manage.py createsuperuser

Запуск сервера

    python manage.py runserver