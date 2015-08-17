# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0020_auto_20150817_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='landline_1',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='landline_2',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
