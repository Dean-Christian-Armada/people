# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0049_auto_20150819_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='number',
            new_name='contact',
        ),
    ]
