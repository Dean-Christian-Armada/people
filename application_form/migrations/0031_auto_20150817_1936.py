# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0030_auto_20150817_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldata',
            name='flags',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='training_certificates',
        ),
    ]
