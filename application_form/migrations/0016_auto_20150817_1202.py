# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0015_auto_20150817_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appdetails',
            name='sea_service',
        ),
        migrations.AddField(
            model_name='appform',
            name='sea_service',
            field=models.ForeignKey(default=None, to='application_form.SeaService'),
        ),
    ]
