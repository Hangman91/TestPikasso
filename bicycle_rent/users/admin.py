from django.contrib import admin
from .models import User



class UserAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'email', 'first_last_name', 'rent_now') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('email', 'first_last_name') 


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(User, UserAdmin)  