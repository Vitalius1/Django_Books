# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-17 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='in_print',
            field=models.BooleanField(default=True),
        ),
    ]