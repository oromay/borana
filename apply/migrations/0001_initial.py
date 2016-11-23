# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='Почта')),
                ('Project', models.FileField(blank=True, upload_to='', verbose_name='Проект')),
                ('Money', models.FileField(blank=True, upload_to='', verbose_name='Смета проекта')),
                ('CV', models.FileField(blank=True, upload_to='', verbose_name='Резюме')),
            ],
        ),
    ]
