# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0042_personaldata_birth_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appsource',
            name='appdetails',
        ),
        migrations.AddField(
            model_name='appdetails',
            name='appdetails',
            field=models.OneToOneField(default=None, to='application_form.AppSource'),
        ),
    ]
