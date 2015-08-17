# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0023_auto_20150817_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highschool',
            name='_from',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='highschool',
            name='_to',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tertiary',
            name='_from',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tertiary',
            name='_to',
            field=models.IntegerField(),
        ),
    ]
