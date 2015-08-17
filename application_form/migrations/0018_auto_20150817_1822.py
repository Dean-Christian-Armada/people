# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0017_auto_20150817_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldata',
            old_name='email_address',
            new_name='email_address_1',
        ),
        migrations.RenameField(
            model_name='personaldata',
            old_name='landline',
            new_name='landline_1',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='email_address_2',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='landline_2',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='alternative_position',
            field=models.CharField(default=None, max_length=50, choices=[(b'Captain', b'Captain'), (b'Chief Mate', b'Chief Mate'), (b'Chief Engineer', b'Chief Engineer'), (b'2nd Engineer', b'2nd Engineer')]),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='position_applied',
            field=models.CharField(default=None, max_length=50, choices=[(b'Captain', b'Captain'), (b'Chief Mate', b'Chief Mate'), (b'Chief Engineer', b'Chief Engineer'), (b'2nd Engineer', b'2nd Engineer')]),
        ),
    ]
