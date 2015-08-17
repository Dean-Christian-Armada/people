# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0008_auto_20150817_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='name',
            field=models.CharField(default=b'dean', max_length=100),
        ),
        migrations.AlterField(
            model_name='sample',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'signatures', blank=True),
        ),
    ]
