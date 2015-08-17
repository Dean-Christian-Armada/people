# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0021_auto_20150817_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldata',
            old_name='current_address',
            new_name='current_baranggay',
        ),
        migrations.RenameField(
            model_name='personaldata',
            old_name='permanent_address',
            new_name='current_municipality',
        ),
        migrations.RenameField(
            model_name='personaldata',
            old_name='current_address_zip',
            new_name='current_zip',
        ),
        migrations.RenameField(
            model_name='personaldata',
            old_name='permanent_address_zip',
            new_name='permanent_zip',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='current_street',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='current_town',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='permanent_baranggay',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='permanent_municipality',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='permanent_street',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='permanent_town',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='pagibig',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='philhealth',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='sss',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='tin',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
