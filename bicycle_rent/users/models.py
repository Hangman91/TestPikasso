from django.contrib.auth.models import AbstractUser
from django.db import models
#from bicycle.models import Bicycle

class User(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
        blank=False,
        null=False,
    )
    first_last_name = models.CharField(
        'Имя пользователя',
        max_length=150,
        blank=True
    )
    rent_now = models.BooleanField(
        verbose_name='С велосипедом ли в данный момент',
        default=False
    )
    bicycle_now = models.ForeignKey(
        'bicycle.Bicycle',
        on_delete=models.CASCADE,
   #     related_name='rent',
        verbose_name='Велосипед',
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_last_name 