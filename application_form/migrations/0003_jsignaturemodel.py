# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0002_auto_20150817_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSignatureModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', jsignature.fields.JSignatureField(null=True, verbose_name='Signature', blank=True)),
                ('signature_date', models.DateTimeField(null=True, verbose_name='Signature date', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
