# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0003_jsignaturemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'signatures', blank=True)),
            ],
        ),
    ]
