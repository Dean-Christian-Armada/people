# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0002_auto_20150902_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatedModifiedFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='flags',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='flags',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='flags',
            name='id',
        ),
        migrations.AddField(
            model_name='flags',
            name='createdmodifiedfields_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='application_form.CreatedModifiedFields'),
            preserve_default=False,
        ),
    ]
