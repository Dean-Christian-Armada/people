# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0004_auto_20150902_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createdmodifiedfields',
            name='ss',
        ),
        migrations.RemoveField(
            model_name='flags',
            name='createdmodifiedfields_ptr',
        ),
        migrations.RemoveField(
            model_name='vesselname',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='vesselname',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='vesselname',
            name='id',
        ),
        migrations.AddField(
            model_name='createdmodifiedfields',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='createdmodifiedfields',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='flags',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=2, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vesselname',
            name='createdmodifiedfields_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='application_form.CreatedModifiedFields'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flags',
            name='flags',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
