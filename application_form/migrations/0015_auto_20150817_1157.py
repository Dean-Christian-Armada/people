# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0014_auto_20150817_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signature',
            name='app_details',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='form_reference',
        ),
        migrations.AddField(
            model_name='appform',
            name='signature',
            field=models.ImageField(default=None, upload_to=b'signatures', blank=True),
        ),
        migrations.DeleteModel(
            name='Signature',
        ),
    ]
