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
                ('picture', models.ImageField(upload_to=b'application_pictures', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('essay', models.TextField(default=None)),
                ('signature', models.ImageField(default=None, upload_to=b'signatures')),
                ('app_details', models.OneToOneField(to='application_form.AppDetails')),
            ],
        ),
        migrations.CreateModel(
            name='AppSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(default=None, max_length=50)),
                ('specify', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visa_application', models.BooleanField()),
                ('detained', models.BooleanField()),
                ('disciplinary_action', models.BooleanField()),
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
                ('coc', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField()),
                ('rank', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(default=None, max_length=100)),
                ('degree_obtained', models.CharField(default=None, max_length=50)),
                ('coll_from', models.DateField()),
                ('coll_to', models.DateField()),
            ],
        ),
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
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college', models.OneToOneField(to='application_form.College')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100)),
                ('contact', models.CharField(default=None, max_length=100)),
                ('relationship', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('baranggay', models.CharField(default=None, max_length=50)),
                ('town', models.CharField(default=None, max_length=50)),
                ('municipality', models.CharField(default=None, max_length=50)),
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
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(default=None, max_length=100)),
                ('hs_from', models.DateField()),
                ('hs_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license', models.CharField(default=None, unique=True, max_length=50)),
                ('rank', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passport', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField()),
                ('place', models.CharField(default=None, max_length=50)),
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
            name='PersonalData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('middle_name', models.CharField(default=None, max_length=50)),
                ('age', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(default=None, max_length=50)),
                ('landline_1', models.IntegerField(null=True)),
                ('mobile_1', models.CharField(max_length=50, null=True)),
                ('email_address_1', models.EmailField(max_length=254, null=True)),
                ('landline_2', models.IntegerField(default=None, null=True, blank=True)),
                ('mobile_2', models.CharField(max_length=50, null=True, blank=True)),
                ('email_address_2', models.EmailField(default=None, max_length=254, null=True, blank=True)),
                ('preferred_vessel_type', models.CharField(default=None, max_length=50)),
                ('availability_date', models.DateField()),
                ('sss', models.CharField(default=None, max_length=50)),
                ('philhealth', models.CharField(default=None, max_length=50)),
                ('tin', models.CharField(default=None, max_length=50)),
                ('pagibig', models.CharField(default=None, max_length=50)),
                ('civil_status', models.CharField(default=None, max_length=50, choices=[(b'Civil Status', b'Civil Status'), (b'M', b'Married'), (b'S', b'Single')])),
                ('married_date', models.DateField(default=None, null=True)),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('mother_name', models.CharField(max_length=100, null=True)),
                ('current_address', models.ForeignKey(default=None, to='application_form.CurrentAddress')),
                ('permanent_address', models.ForeignKey(default=None, to='application_form.PermanentAddress')),
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
                ('sbook', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField()),
                ('place', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SchengenVisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.BooleanField()),
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
                ('dwt', models.IntegerField(default=None)),
                ('year_built', models.IntegerField()),
                ('engine_type', models.CharField(default=None, max_length=50)),
                ('hp', models.IntegerField()),
                ('kw', models.IntegerField(default=None)),
                ('manning_agency', models.CharField(default=None, max_length=50)),
                ('principal', models.CharField(default=None, max_length=50)),
                ('date_joined', models.DateField()),
                ('date_left', models.DateField()),
                ('duration', models.IntegerField()),
                ('rank', models.CharField(default=None, max_length=50)),
                ('cause_of_discharge', models.CharField(default=None, max_length=100)),
                ('app_form', models.ForeignKey(default=None, to='application_form.AppForm')),
            ],
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('birthdate', models.DateField(default=None, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SRC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('src', models.CharField(default=None, unique=True, max_length=50)),
                ('rank', models.CharField(default=None, max_length=50)),
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
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='YellowFever',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yellow_fever', models.IntegerField(unique=True)),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='personaldata',
            name='spouse',
            field=models.ForeignKey(default=None, to='application_form.Spouse'),
        ),
        migrations.AddField(
            model_name='education',
            name='highschool',
            field=models.OneToOneField(to='application_form.HighSchool'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='coc',
            field=models.OneToOneField(to='application_form.COC'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='goc',
            field=models.OneToOneField(to='application_form.GOC'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='license',
            field=models.OneToOneField(to='application_form.License'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='passport',
            field=models.OneToOneField(to='application_form.Passport'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='sbook',
            field=models.OneToOneField(to='application_form.SBook'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='schgengen_visa',
            field=models.OneToOneField(to='application_form.SchengenVisa'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='src',
            field=models.OneToOneField(to='application_form.SRC'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='us_visa',
            field=models.OneToOneField(to='application_form.USVisa'),
        ),
        migrations.AddField(
            model_name='certificatesdocuments',
            name='yellow_fever',
            field=models.OneToOneField(to='application_form.YellowFever'),
        ),
        migrations.AddField(
            model_name='appform',
            name='background_information',
            field=models.OneToOneField(to='application_form.BackgroundInformation'),
        ),
        migrations.AddField(
            model_name='appform',
            name='certificates_documents',
            field=models.OneToOneField(to='application_form.CertificatesDocuments'),
        ),
        migrations.AddField(
            model_name='appform',
            name='education',
            field=models.OneToOneField(to='application_form.Education'),
        ),
        migrations.AddField(
            model_name='appform',
            name='emergency_contact',
            field=models.OneToOneField(to='application_form.EmergencyContact'),
        ),
        migrations.AddField(
            model_name='appform',
            name='flags',
            field=models.ManyToManyField(to='application_form.FlagDocuments'),
        ),
        migrations.AddField(
            model_name='appform',
            name='personal_data',
            field=models.OneToOneField(to='application_form.PersonalData'),
        ),
        migrations.AddField(
            model_name='appform',
            name='reference',
            field=models.OneToOneField(default=None, to='application_form.Reference'),
        ),
        migrations.AddField(
            model_name='appform',
            name='training_certificates',
            field=models.ManyToManyField(to='application_form.TrainingCertificates'),
        ),
        migrations.AddField(
            model_name='appdetails',
            name='appdetails',
            field=models.OneToOneField(default=None, to='application_form.AppSource'),
        ),
    ]
