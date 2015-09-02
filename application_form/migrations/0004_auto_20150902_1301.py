# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0003_auto_20150902_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createdmodifiedfields',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='createdmodifiedfields',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='createdmodifiedfields',
            name='ss',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flags',
            name='flags',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
