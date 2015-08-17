# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsource',
            name='source',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='sea_service',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='sea_service',
            field=models.ForeignKey(default=None, to='application_form.SeaService'),
        ),
        migrations.DeleteModel(
            name='Source',
        ),
    ]
