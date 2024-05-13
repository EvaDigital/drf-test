# drf-test

## Architecture and technology
### Modules

1. **kaspi_backend**
Contains:
```sh
- kaspi_backend
 -- settings.py
 -- urls.py
 -- celery.py
```
Description: This is the main directory containing your Django project.

1.1 **settings.py**
Is the main settings file for Django project. It contains all the settings required for your Django application to work.

The settings.py file defines settings such as database, authentication settings, static file settings, security keys, and more.

This file defines the configuration of your project, and changes here affect the entire application in the project.

2. **landing**
3. **stores**
4. **users**


# Инструкция по установке и запуску проекта

Следуйте этим шагам, чтобы установить и запустить проект.

## Рабочая дерриктория
```bash 
  git clone https://github.com/EvaDigital/drf-test.git
  cd drf-test
```

## Шаг 1: Создать .env файл

Создайте файл с именем `.env` в корневой директории проекта и заполните его данными по примеру из файла `.env_template`.

## Шаг 2: Запустить Docker-контейнеры

Выполните следующую команду, чтобы запустить Docker-контейнеры: 
``` bash 
  docker-compose up -d
```
## Шаг 3: Создать миграции базы данных

Выполните следующие команды, чтобы создать миграции базы данных:
``` bash 
  docker exec drf-test-web-1 python manage.py makemigrations
  docker exec drf-test-web-1 python manage.py migrate
```

## Шаг 5: Создать администратора

Выполните следующую команду, чтобы создать администратора с указанным именем пользователя и паролем:
``` bash 
  docker exec drf-test-web-1 python manage.py add_admin <username> <password>
```

## Шаг 6: Перейти в админ-панель

Откройте браузер и перейдите по адресу:
``` bash 
  http://localhost:8000/admin/
```
Войдите с использованием созданных учетных данных администратора и создайте тестовые данные.


## API Endpoints
All API requests should be made to:
```
http://localhost:8080/api
```

### `/advert-list/` (GET)

Получение списка объявлений

#### Request

- Method: GET
- URL: `/advert-list/`

#### Response

- Status Code: 200

```json
[
    {
        "id": 1,
        "city": {
            "name": "krakow"
        },
        "category": {
            "name": "test 1"
        },
        "created": "2023-10-02T15:50:03.874711Z",
        "title": "advert - 1",
        "description": "desc advert - 1",
        "views": 2
    },
  ...
]
```

### `/advert/<id>/` (GET)

Получение информации об объявлении используйте следующий запрос, заменив `<id>` на идентификатор объявления

#### Request

- Method: GET
- URL: `/advert/<id>/`

#### Response

- Status Code: 200

```json
{
    "id": 1,
    "city": {
        "name": "krakow"
    },
    "category": {
        "name": "test 1"
    },
    "created": "2023-10-02T15:50:03.874711Z",
    "title": "advert - 1",
    "description": "desc advert - 1",
    "views": 3
}
```



## Запуск тестов

Чтобы запустить тесты, убедитесь, что вы заменили `DB_USER` в файле `.env` на `root`, затем выполните следующую команду:
``` bash
  docker exec drf-test-web-1 python manage.py test adverts
```

Эти инструкции помогут вам настроить, запустить проект и выполнить тесты.


