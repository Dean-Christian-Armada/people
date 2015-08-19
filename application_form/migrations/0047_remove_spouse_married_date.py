# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0046_auto_20150819_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spouse',
            name='married_date',
        ),
    ]
