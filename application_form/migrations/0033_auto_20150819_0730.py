# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0032_auto_20150819_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdetails',
            name='alternative_position',
            field=models.CharField(default=b'Alternative Position', max_length=50, choices=[(b'Captain', b'Captain'), (b'Chief Mate', b'Chief Mate'), (b'Chief Engineer', b'Chief Engineer'), (b'2nd Engineer', b'2nd Engineer')]),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='position_applied',
            field=models.CharField(default=b'Position Applied', max_length=50, choices=[(b'Captain', b'Captain'), (b'Chief Mate', b'Chief Mate'), (b'Chief Engineer', b'Chief Engineer'), (b'2nd Engineer', b'2nd Engineer')]),
        ),
    ]
