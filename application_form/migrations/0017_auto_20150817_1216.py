# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0016_auto_20150817_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appform',
            name='sea_service',
        ),
        migrations.AddField(
            model_name='seaservice',
            name='app_form',
            field=models.ForeignKey(default=None, to='application_form.AppForm'),
        ),
    ]
