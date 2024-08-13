# TestPikasso

Тестовое задание для Пикассо.

Для локального запуска проекта:

*Создаём окружение*
```
python -m venv venv
```

*Запускаем окружение*
```
source venv/Scripts/activate
```

*Устанавливаем зависимости*
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

*Миграции*
```python manage.py makemigrations
python manage.py migrate
```

*Локальный запуск*
```
python manage.py runserver
```


*Спецификацию по api можно получить по ссылке: *
```
http://127.0.0.1:8000/swagger/
```

Примеры запросов:  
  
Регистрация нового пользователя:
```
http://127.0.0.1:8000/auth/users/
  
{  
    "email": "asas@asas.ru",  
    "first_last_name": "ПУпкин Вася",  
    "password": "123123Ffddf"  
}  
```
Создание токена:
```
http://127.0.0.1:8000/auth/jwt/create
  
{  
    "email": "asas@asas.ru",  
    "password": "123123Ffddf"  
}
```
  
Список свободных велосипедов (GET-запрос): 
```
http://127.0.0.1:8000/api/bicycle/
```

Аренда велосипеда с pk=2 (POST-запрос): 
```
http://127.0.0.1:8000/api/bicycle/2/
```
  
Конец аренды (POST-запрос):
```
http://127.0.0.1:8000/api/bicycle/stop/
```
  
Список сессий пользователя (GET-запрос):
``` 
http://127.0.0.1:8000/api/rent/9/
```
