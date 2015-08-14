# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application_date', models.DateField()),
                ('position_applied', models.CharField(default=None, max_length=50)),
                ('alternative_position', models.CharField(default=None, max_length=50)),
                ('picture', models.ImageField(upload_to=b'application_images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('form_reference', models.CharField(default=None, max_length=50)),
                ('essay', models.TextField(default=None)),
                ('app_details', models.ForeignKey(to='application_form.AppDetails')),
            ],
        ),
        migrations.CreateModel(
            name='AppSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specify', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visa_application', models.BooleanField(default=0)),
                ('detained', models.BooleanField(default=0)),
                ('disciplinary_action', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CertificatesDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='COC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coc', models.IntegerField(unique=True)),
                ('issued', models.DateField()),
                ('expiry', models.DateField()),
                ('rank', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100)),
                ('relationship', models.CharField(default=None, max_length=50)),
                ('address', models.CharField(default=None, max_length=100)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FlagDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flags', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GOC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goc', models.CharField(default=None, unique=True, max_length=50)),
                ('issued', models.DateField()),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(default=None, max_length=100)),
                ('_from', models.DateField()),
                ('_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license', models.CharField(default=None, unique=True, max_length=50)),
                ('issued', models.DateField()),
                ('rank', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passport', models.IntegerField(unique=True)),
                ('issued', models.DateField()),
                ('expiry', models.DateField()),
                ('place', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('middle_name', models.CharField(default=None, max_length=50)),
                ('age', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('landline', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('preferred_vessel_type', models.CharField(default=None, max_length=50)),
                ('availability_date', models.DateField()),
                ('sss', models.IntegerField()),
                ('philhealth', models.IntegerField()),
                ('tin', models.IntegerField()),
                ('pagibig', models.IntegerField()),
                ('permanent_address', models.CharField(default=None, max_length=50)),
                ('permanent_address_zip', models.IntegerField()),
                ('current_address', models.CharField(default=None, max_length=50)),
                ('current_address_zip', models.IntegerField()),
                ('flags', models.ManyToManyField(to='application_form.FlagDocuments')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('verified_by', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('date', models.DateField()),
                ('company_name', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('person_contacted', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('veracity_history', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('health_problem', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('financial_liability', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('character', models.TextField(null=True, blank=True)),
                ('comments', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sbook', models.IntegerField(unique=True)),
                ('issued', models.DateField()),
                ('expiry', models.DateField()),
                ('place', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SchengenVisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.BooleanField()),
                ('place_issued', models.CharField(default=None, max_length=50)),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SeaService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vessel_name', models.CharField(default=None, max_length=50)),
                ('vessel_type', models.CharField(default=None, max_length=50)),
                ('flag', models.CharField(default=None, max_length=50)),
                ('grt', models.IntegerField()),
                ('year_built', models.IntegerField()),
                ('engine_type', models.CharField(default=None, max_length=50)),
                ('hp', models.IntegerField()),
                ('manning_agency', models.CharField(default=None, max_length=50)),
                ('principal', models.CharField(default=None, max_length=50)),
                ('date_joined', models.DateField()),
                ('date_left', models.DateField()),
                ('duration', models.IntegerField()),
                ('rank', models.CharField(default=None, max_length=50)),
                ('cause_of_discharge', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SRC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('src', models.CharField(default=None, unique=True, max_length=50)),
                ('issued', models.DateField()),
                ('rank', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tertiary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(default=None, max_length=100)),
                ('degree_obtained', models.CharField(default=None, max_length=50)),
                ('_from', models.DateField()),
                ('_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCertificates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trainings_certificates', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='USVisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.BooleanField()),
                ('place_issued', models.CharField(default=None, max_length=50)),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='YellowFever',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yellow_fever', models.IntegerField(unique=True)),
                ('place_issued', models.CharField(default=None, max_length=50)),
                ('issued', models.DateField()),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='personaldata',
            name='sea_service',
            field=models.ManyToManyField(to='application_form.SeaService'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='training_certificates',
            field=models.ManyToManyField(to='application_form.TrainingCertificates'),
        ),
        migrations.AddField(
            model_name='education',
            name='highschool',
            field=models.ForeignKey(to='application_form.HighSchool'),
        ),
        migrations.AddField(
            model_name='education',
            name='tertiary',
            field=models.ForeignKey(to='application_form.Tertiary'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='coc',
            field=models.ForeignKey(to='application_form.COC'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='goc',
            field=models.ForeignKey(to='application_form.GOC'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='license',
            field=models.ForeignKey(to='application_form.License'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='passport',
            field=models.ForeignKey(to='application_form.Passport'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='sbook',
            field=models.ForeignKey(to='application_form.SBook'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='schgengen_visa',
            field=models.ForeignKey(to='application_form.SchengenVisa'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='src',
            field=models.ForeignKey(to='application_form.SRC'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='us_visa',
            field=models.ForeignKey(to='application_form.USVisa'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='yellow_fever',
            field=models.ForeignKey(to='application_form.YellowFever'),
        ),
        migrations.AddField(
            model_name='appsource',
            name='source',
            field=models.ForeignKey(to='application_form.Source'),
        ),
        migrations.AddField(
            model_name='appform',
            name='background_information',
            field=models.ForeignKey(to='application_form.BackgroundInformation'),
        ),
        migrations.AddField(
            model_name='appform',
            name='certificates_documents',
            field=models.ForeignKey(to='application_form.CertificatesDocuments'),
        ),
        migrations.AddField(
            model_name='appform',
            name='education',
            field=models.ForeignKey(to='application_form.Education'),
        ),
        migrations.AddField(
            model_name='appform',
            name='emergency_contact',
            field=models.ForeignKey(to='application_form.EmergencyContact'),
        ),
        migrations.AddField(
            model_name='appform',
            name='personal_data',
            field=models.ForeignKey(to='application_form.PersonalData'),
        ),
        migrations.AddField(
            model_name='appform',
            name='reference',
            field=models.ForeignKey(default=None, to='application_form.Reference'),
        ),
        migrations.AddField(
            model_name='appdetails',
            name='appsource',
            field=models.ForeignKey(to='application_form.AppSource'),
        ),
    ]
