# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0009_auto_20150817_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsignaturemodel',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
