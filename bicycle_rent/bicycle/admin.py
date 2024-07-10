from django.contrib import admin
from .models import Bicycle, Rent



class BicycleAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'is_free') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('id', 'is_free') 
    # Добавляем возможность фильтрации по дате
    list_filter = ('id', 'is_free') 

class RentAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('client', 'bicycle', 'rent_start_time', 'rent_stop_time') 
    # Добавляем интерфейс для поиска по тексту постов

admin.site.register(Bicycle, BicycleAdmin)  
admin.site.register(Rent, RentAdmin) 