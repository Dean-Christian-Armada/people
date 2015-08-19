# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0040_auto_20150819_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='email_address_1',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='landline_1',
            field=models.IntegerField(null=True),
        ),
    ]
