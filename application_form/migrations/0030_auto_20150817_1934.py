# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0029_auto_20150817_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='appform',
            name='flags',
            field=models.ManyToManyField(to='application_form.FlagDocuments'),
        ),
        migrations.AddField(
            model_name='appform',
            name='training_certificates',
            field=models.ManyToManyField(to='application_form.TrainingCertificates'),
        ),
    ]
