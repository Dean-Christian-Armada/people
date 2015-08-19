# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0050_auto_20150819_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='coll_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='college',
            name='coll_to',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='highschool',
            name='hs_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='highschool',
            name='hs_to',
            field=models.DateField(),
        ),
    ]
