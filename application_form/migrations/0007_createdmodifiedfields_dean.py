# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0006_remove_vesselname_vessel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='createdmodifiedfields',
            name='dean',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
