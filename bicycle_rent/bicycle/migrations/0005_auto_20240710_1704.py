# Generated by Django 2.2.19 on 2024-07-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicycle', '0004_auto_20240710_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='rent_stop_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время начала'),
        ),
    ]
