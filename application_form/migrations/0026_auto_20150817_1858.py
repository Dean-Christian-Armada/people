# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0025_emergencycontact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='number',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
