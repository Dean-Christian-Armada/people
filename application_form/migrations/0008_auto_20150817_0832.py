# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0007_sample_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='name',
            field=models.CharField(default=b'dean', max_length=100, blank=True),
        ),
    ]
