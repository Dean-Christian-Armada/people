# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0035_auto_20150819_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appdetails',
            name='appsource',
        ),
        migrations.AddField(
            model_name='appsource',
            name='appdetails',
            field=models.ForeignKey(default=None, to='application_form.AppDetails'),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='alternative_position',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='position_applied',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='highschool',
            field=models.OneToOneField(to='application_form.HighSchool'),
        ),
        migrations.AlterField(
            model_name='education',
            name='tertiary',
            field=models.OneToOneField(to='application_form.Tertiary'),
        ),
    ]
