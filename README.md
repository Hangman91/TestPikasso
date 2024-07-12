# TestPikasso

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