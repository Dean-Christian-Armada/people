# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0007_createdmodifiedfields_dean'),
    ]

    operations = [
        migrations.AddField(
            model_name='vesselname',
            name='vessel_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
