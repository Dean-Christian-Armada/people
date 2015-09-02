# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0008_vesselname_vessel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vesselname',
            name='createdmodifiedfields_ptr',
        ),
        migrations.AddField(
            model_name='flags',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='flags',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='vesselname',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='vesselname',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='vesselname',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=None, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CreatedModifiedFields',
        ),
    ]
