# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0024_auto_20150817_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencycontact',
            name='number',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
