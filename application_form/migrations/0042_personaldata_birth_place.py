# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0041_auto_20150819_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='birth_place',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
