# Table Reservation Service

API-сервис для бронирования столиков в ресторане.

## Описание проекта
Сервис предоставляет REST API для:
- управления столиками (CRUD)
- создания и удаления броней
- проверки пересечения временных слотов броней

Проект выполнен на Django + Django REST Framework и PostgreSQL, упакован в Docker.

## Технологии
- Python 3.10
- Django 5.2
- Django REST Framework
- PostgreSQL 14
- Docker, Docker Compose
- pytest, pytest-django для тестирования
- python-dotenv для работы с переменными окружения

## Быстрый старт

1. Склонируйте репозиторий:
   ```bash
   git clone git@github.com:UsmanSakhbeev/table_reservations.git
   cd table_reservations
   ```

2. Создайте файл `.env` в корне проекта:
   ```dotenv
   DJANGO_SECRET_KEY=your_secret_key_here
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgres://postgres:postgres@db:5432/restaurant_db
   ```

3. Запустите проект с помощью Docker Compose:
   ```bash
   docker-compose up --build
   ```
   - Веб-сервис будет доступен по адресу `http://localhost:8000/`.
   - API-эндпоинты:
     - `GET  /api/tables/` — список столиков
     - `POST /api/tables/` — создать столик
     - `DELETE /api/tables/{id}/` — удалить столик
     - `GET  /api/reservations/` — список броней
     - `POST /api/reservations/` — создать бронь
     - `DELETE /api/reservations/{id}/` — удалить бронь

4. Остановка контейнеров:
   ```bash
   docker-compose down
   ```

## Тестирование

Для запуска набора автоматических тестов выполните в контейнере:
```bash
docker-compose exec web pytest
```

## Логи

По умолчанию логи приложения пишутся в файл `app.log` и выводятся в консоль.

## Переменные окружения

- `DJANGO_SECRET_KEY` — секретный ключ Django
- `DJANGO_DEBUG` — режим отладки (`True`/`False`)
- `DJANGO_ALLOWED_HOSTS` — список разрешённых хостов, разделённых запятыми
- `DATABASE_URL` — URL подключения к базе данных

---
