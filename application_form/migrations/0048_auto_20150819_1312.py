# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0047_remove_spouse_married_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tertiary',
            new_name='College',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='tertiary',
            new_name='college',
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='father_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='married_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='mobile_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='mother_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='birthdate',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
