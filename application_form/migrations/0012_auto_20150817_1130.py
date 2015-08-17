# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0011_jsignaturemodel_signatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsignaturemodel',
            name='signatures',
            field=models.ImageField(default=None, upload_to=b'model/signatures', blank=True),
        ),
    ]
