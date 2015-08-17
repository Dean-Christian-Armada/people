# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0005_auto_20150817_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='name',
        ),
        migrations.AddField(
            model_name='sample',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'signatures'),
        ),
    ]
