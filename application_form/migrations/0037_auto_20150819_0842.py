# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0036_auto_20150819_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appform',
            name='app_details',
            field=models.OneToOneField(to='application_form.AppDetails'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='background_information',
            field=models.OneToOneField(to='application_form.BackgroundInformation'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='certificates_documents',
            field=models.OneToOneField(to='application_form.CertificatesDocuments'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='education',
            field=models.OneToOneField(to='application_form.Education'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='emergency_contact',
            field=models.OneToOneField(to='application_form.EmergencyContact'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='personal_data',
            field=models.OneToOneField(to='application_form.PersonalData'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='reference',
            field=models.OneToOneField(default=None, to='application_form.Reference'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='coc',
            field=models.OneToOneField(to='application_form.COC'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='goc',
            field=models.OneToOneField(to='application_form.GOC'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='license',
            field=models.OneToOneField(to='application_form.License'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='passport',
            field=models.OneToOneField(to='application_form.Passport'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='sbook',
            field=models.OneToOneField(to='application_form.SBook'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='schgengen_visa',
            field=models.OneToOneField(to='application_form.SchengenVisa'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='src',
            field=models.OneToOneField(to='application_form.SRC'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='us_visa',
            field=models.OneToOneField(to='application_form.USVisa'),
        ),
        migrations.AlterField(
            model_name='certificatesdocuments',
            name='yellow_fever',
            field=models.OneToOneField(to='application_form.YellowFever'),
        ),
    ]
