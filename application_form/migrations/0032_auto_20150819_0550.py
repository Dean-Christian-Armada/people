# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0031_auto_20150817_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(default=None, max_length=50)),
                ('baranggay', models.CharField(default=None, max_length=50)),
                ('town', models.CharField(default=None, max_length=50)),
                ('municipality', models.CharField(default=None, max_length=50)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(default=None, max_length=50)),
                ('baranggay', models.CharField(default=None, max_length=50)),
                ('town', models.CharField(default=None, max_length=50)),
                ('municipality', models.CharField(default=None, max_length=50)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('birthdate', models.DateField(default=None, null=True, blank=True)),
                ('contact', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('married_date', models.DateField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='current_baranggay',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='current_municipality',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='current_street',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='current_town',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='current_zip',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='permanent_baranggay',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='permanent_municipality',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='permanent_street',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='permanent_town',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='permanent_zip',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='spouse_birthdate',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='spouse_contact',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='spouse_name',
        ),
        migrations.AddField(
            model_name='seaservice',
            name='dwt',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='seaservice',
            name='kw',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='alternative_position',
            field=models.CharField(default=None, max_length=50, choices=[(b'Position Applied For', b'Position Applied For'), (b'Captain', b'Captain'), (b'Chief Mate', b'Chief Mate'), (b'Chief Engineer', b'Chief Engineer'), (b'2nd Engineer', b'2nd Engineer')]),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='position_applied',
            field=models.CharField(default=None, max_length=50, choices=[(b'Position Applied For', b'Position Applied For'), (b'Captain', b'Captain'), (b'Chief Mate', b'Chief Mate'), (b'Chief Engineer', b'Chief Engineer'), (b'2nd Engineer', b'2nd Engineer')]),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='current_address',
            field=models.ForeignKey(default=None, to='application_form.CurrentAddress'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='permanent_address',
            field=models.ForeignKey(default=None, to='application_form.PermanentAddress'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='spouse',
            field=models.ForeignKey(default=None, to='application_form.Spouse'),
        ),
    ]
