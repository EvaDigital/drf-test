# drf-test

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
http://localhost:8080/
```

### `/attack` (POST)

Initiates a new attack with the provided package identifiers and target id.

#### Request

- Method: POST
- URL: `/attack`
- Body: JSON object. targetId (required), url - full attack url (required), packages (required)

```json
{
  "targetId": "123e4567-e89b-12d3-a456-426614174000",
  "url": "https://tankbattlemania.com/operation-pillowfight",
  "packages": [
    "123e4567-e89b-12d3-a456-426614174000",
    "123e4567-e89b-12d3-a456-426614174000",
    "..."
  ]
}
```

#### Response

- Status Code: 201 (Created)
- Body: JSON object representing the package information (as per `IPackageInfo` structure)

```json
{
  "attackId": "123e4567-e89b-12d3-a456-426614174000",
  "status": "pending"
}
```

## Шаг 7: Получить список объявлений

Для получения списка объявлений используйте следующий запрос:
``` bash 
  GET /api/advert-list/
```

## Шаг 8: Получить информацию об объявлении

Для получения информации об объявлении используйте следующий запрос, заменив `<id>` на идентификатор объявления:
``` bash
  GET /api/advert/<id>/
```

## Запуск тестов

Чтобы запустить тесты, убедитесь, что вы заменили `DB_USER` в файле `.env` на `root`, затем выполните следующую команду:
``` bash
  docker exec drf-test-web-1 python manage.py test adverts
```

Эти инструкции помогут вам настроить, запустить проект и выполнить тесты.


