# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0010_jsignaturemodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsignaturemodel',
            name='signatures',
            field=models.ImageField(default=None, upload_to=b'signatures', blank=True),
        ),
    ]
