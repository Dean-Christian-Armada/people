# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0013_auto_20150817_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.ImageField(default=None, upload_to=b'signatures', blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='JSignatureModel',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='sea_service',
        ),
        migrations.AddField(
            model_name='appdetails',
            name='sea_service',
            field=models.ForeignKey(default=None, to='application_form.SeaService'),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='picture',
            field=models.ImageField(upload_to=b'application_pictures', blank=True),
        ),
        migrations.AddField(
            model_name='signature',
            name='app_details',
            field=models.OneToOneField(to='application_form.AppDetails'),
        ),
    ]
