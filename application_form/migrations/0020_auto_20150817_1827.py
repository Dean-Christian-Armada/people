# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0019_auto_20150817_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='landline_2',
            field=models.IntegerField(default=None),
        ),
    ]
