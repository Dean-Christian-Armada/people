# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0048_auto_20150819_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='_from',
            new_name='coll_from',
        ),
        migrations.RenameField(
            model_name='college',
            old_name='_to',
            new_name='coll_to',
        ),
        migrations.RenameField(
            model_name='highschool',
            old_name='_from',
            new_name='hs_from',
        ),
        migrations.RenameField(
            model_name='highschool',
            old_name='_to',
            new_name='hs_to',
        ),
    ]
