# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quarto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='numero',
        ),
        migrations.AddField(
            model_name='quarto',
            name='numero',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
