# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0034_auto_20150819_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdetails',
            name='position_applied',
            field=models.CharField(default=b'Chief Mate', max_length=50, choices=[(b'Captain', b'Captain'), (b'Chief Mate', b'Chief Mate'), (b'Chief Engineer', b'Chief Engineer'), (b'2nd Engineer', b'2nd Engineer')]),
        ),
    ]
