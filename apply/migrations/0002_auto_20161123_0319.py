# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='Money',
            field=models.FileField(blank=True, upload_to='attachments', verbose_name='Смета проекта'),
        ),
    ]