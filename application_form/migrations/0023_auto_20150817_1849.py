# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0022_auto_20150817_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='civil_status',
            field=models.CharField(default=None, max_length=50, null=True, blank=True, choices=[(b'M', b'Married'), (b'S', b'Single')]),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='father_name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='married_date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='mother_name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='spouse_birthdate',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='spouse_contact',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='spouse_name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
    ]
