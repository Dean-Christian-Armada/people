# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0027_auto_20150817_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coc',
            name='issued',
        ),
        migrations.RemoveField(
            model_name='goc',
            name='issued',
        ),
        migrations.RemoveField(
            model_name='license',
            name='issued',
        ),
        migrations.RemoveField(
            model_name='passport',
            name='issued',
        ),
        migrations.RemoveField(
            model_name='sbook',
            name='issued',
        ),
        migrations.RemoveField(
            model_name='src',
            name='issued',
        ),
    ]
