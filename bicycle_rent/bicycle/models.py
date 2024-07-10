from django.db import models
from users.models import User
from django.utils import timezone


class Bicycle(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID велосипеда',
        unique=True,
    )
    is_free = models.BooleanField(
        verbose_name='Свободен ли в данный момент'
    )
    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипед'


class Rent(models.Model):

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rent',
        verbose_name='Пользователь'
    )
    bicycle = models.ForeignKey(
        Bicycle,
        on_delete=models.CASCADE,
        related_name='rent',
        verbose_name='Велосипед'
    )
    rent_start_time = models.DateTimeField(
        verbose_name='Время начала',
        default=timezone.now,
    )
    rent_stop_time = models.DateTimeField(
        verbose_name='Время конца',
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = 'Сессия аренды'
        verbose_name_plural = 'Сессия аренды'