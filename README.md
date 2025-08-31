# API Yatube

## 📌 Описание проекта
**Yatube API** — это учебный проект социальной сети для публикации постов, комментариев и подписок на авторов.  
Проект реализует **REST API** для взаимодействия с данными Yatube, поддерживает регистрацию пользователей, JWT-аутентификацию и полный CRUD-функционал для работы с постами и комментариями.

Основные возможности:
- 🔑 Регистрация и аутентификация пользователей (JWT)
- 📝 CRUD для постов
- 💬 CRUD для комментариев
- 👥 Подписки на авторов
- 📂 Работа с группами постов
- ⚡ REST API на базе Django REST Framework

## 🛠 Технологии
- Python 3.9+
- Django 3.2
- Django REST Framework
- Simple JWT
- SQLite (по умолчанию)

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/MaksZakharov/api-yatube.git
   cd api-yatube
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции:
   ```bash
   python manage.py migrate
   ```

5. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

## 🔑 Аутентификация
Используется **JWT-токен**.  
Получить токен:
```http
POST /api/v1/jwt/create/
```
Обновить токен:
```http
POST /api/v1/jwt/refresh/
```
Проверить токен:
```http
POST /api/v1/jwt/verify/
```

## 📚 Примеры запросов
- Получение всех постов:
  ```
  GET /api/v1/posts/
  ```
- Создание поста:
  ```
  POST /api/v1/posts/
  {
    "text": "Мой первый пост!",
    "group": 1
  }
  ```
- Комментарии к посту:
  ```
  GET /api/v1/posts/{post_id}/comments/
  ```

## 🧪 Тестирование
Запуск тестов:
```bash
pytest
```

## 👨‍💻 Автор
Проект выполнен в рамках курса «Python-разработчик плюс» от **Яндекс Практикум**.  
Автор: [Maks Zakharov](https://github.com/MaksZakharov)
