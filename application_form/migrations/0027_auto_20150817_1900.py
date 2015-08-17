# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0026_auto_20150817_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coc',
            name='coc',
            field=models.CharField(default=None, unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='passport',
            name='passport',
            field=models.CharField(default=None, unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sbook',
            name='sbook',
            field=models.CharField(default=None, unique=True, max_length=100),
        ),
    ]
