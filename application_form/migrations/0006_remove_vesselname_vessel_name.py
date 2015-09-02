# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0005_auto_20150902_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vesselname',
            name='vessel_name',
        ),
    ]
