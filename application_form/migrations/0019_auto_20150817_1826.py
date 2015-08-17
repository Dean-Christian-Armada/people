# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0018_auto_20150817_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='mobile_1',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='mobile_2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='email_address_1',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='email_address_2',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='landline_2',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
