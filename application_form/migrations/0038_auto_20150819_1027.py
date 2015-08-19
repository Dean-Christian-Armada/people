# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0037_auto_20150819_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergencycontact',
            name='address',
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='baranggay',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='municipality',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='street',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='town',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
