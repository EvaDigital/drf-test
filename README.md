# drf-test

# Инструкция по установке и запуску проекта

Следуйте этим шагам, чтобы установить и запустить проект.

## Шаг 1: Создать .env файл

Создайте файл с именем `.env` в корневой директории проекта и заполните его данными по примеру из файла `.env_template`.

## Шаг 2: Запустить Docker-контейнеры

Выполните следующую команду, чтобы запустить Docker-контейнеры: 
``` bash 
  docker-compose up -d
```
## Шаг 3: Создать миграции базы данных

Выполните следующую команду, чтобы создать миграции базы данных:
``` bash 
  docker exec drf-test-web-1 python manage.py makemigrations
```

