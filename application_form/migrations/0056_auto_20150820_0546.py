# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0055_auto_20150819_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appform',
            name='signature',
            field=models.ImageField(default=None, upload_to=b'signatures'),
        ),
    ]
