# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0028_auto_20150817_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schengenvisa',
            name='place_issued',
        ),
        migrations.RemoveField(
            model_name='usvisa',
            name='place_issued',
        ),
        migrations.RemoveField(
            model_name='yellowfever',
            name='issued',
        ),
        migrations.RemoveField(
            model_name='yellowfever',
            name='place_issued',
        ),
    ]
