# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150902_1245'),
        ('application_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('barangay', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BirthPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth_place', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CauseOfDischarge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cause_of_discharge', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CivilStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('civil_status', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college', models.CharField(default=None, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(default=None, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detained',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detained', models.NullBooleanField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaryAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disciplinary_action', models.NullBooleanField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engine_type', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flags', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchools',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('highschool', models.CharField(default=None, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManningAgency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manning_agency', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('municipality', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('principal', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reasons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField(default=None, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationship', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specifics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specific', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCertificateDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VesselName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vessel_name', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VesselType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vessel_type', models.CharField(default=None, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisaApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visa_application', models.NullBooleanField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('reason', models.ForeignKey(default=None, to='application_form.Reasons')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.PositiveIntegerField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('barangay', models.ForeignKey(default=None, to='application_form.Barangay')),
                ('municipality', models.ForeignKey(default=None, to='application_form.Municipality')),
            ],
        ),
        migrations.RemoveField(
            model_name='appdetails',
            name='appdetails',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='coc',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='goc',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='license',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='sbook',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='schgengen_visa',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='src',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='us_visa',
        ),
        migrations.RemoveField(
            model_name='certificatesdocuments',
            name='yellow_fever',
        ),
        migrations.RemoveField(
            model_name='education',
            name='college',
        ),
        migrations.RemoveField(
            model_name='education',
            name='highschool',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='app_details',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='background_information',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='certificates_documents',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='education',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='emergency_contact',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='flags',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='personal_data',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='signature',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='training_certificates',
        ),
        migrations.RemoveField(
            model_name='appsource',
            name='specify',
        ),
        migrations.RemoveField(
            model_name='college',
            name='coll_from',
        ),
        migrations.RemoveField(
            model_name='college',
            name='coll_to',
        ),
        migrations.RemoveField(
            model_name='college',
            name='degree_obtained',
        ),
        migrations.RemoveField(
            model_name='college',
            name='school',
        ),
        migrations.RemoveField(
            model_name='currentaddress',
            name='baranggay',
        ),
        migrations.RemoveField(
            model_name='currentaddress',
            name='municipality',
        ),
        migrations.RemoveField(
            model_name='currentaddress',
            name='town',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='baranggay',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='municipality',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='town',
        ),
        migrations.RemoveField(
            model_name='highschool',
            name='hs_from',
        ),
        migrations.RemoveField(
            model_name='highschool',
            name='hs_to',
        ),
        migrations.RemoveField(
            model_name='highschool',
            name='school',
        ),
        migrations.RemoveField(
            model_name='license',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='passport',
            name='place',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='baranggay',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='municipality',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='town',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='married_date',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='spouse',
        ),
        migrations.RemoveField(
            model_name='sbook',
            name='place',
        ),
        migrations.RemoveField(
            model_name='schengenvisa',
            name='type',
        ),
        migrations.RemoveField(
            model_name='seaservice',
            name='app_form',
        ),
        migrations.RemoveField(
            model_name='usvisa',
            name='type',
        ),
        migrations.AddField(
            model_name='appform',
            name='application_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='appform',
            name='application_source',
            field=models.ForeignKey(default=None, to='application_form.AppSource'),
        ),
        migrations.AddField(
            model_name='appform',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='appform',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='appform',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'application/pictures', blank=True),
        ),
        migrations.AddField(
            model_name='appform',
            name='signatures',
            field=models.ImageField(default=None, upload_to=b'application/signatures', blank=True),
        ),
        migrations.AddField(
            model_name='appform',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='appsource',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='coc',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='coc',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='coc',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='college',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='schoolyear_from',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='college',
            name='schoolyear_to',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='college',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='currentaddress',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='flagdocuments',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='flagdocuments',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='goc',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='goc',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='goc',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='highschool',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='highschool',
            name='schoolyear_from',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='highschool',
            name='schoolyear_to',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='highschool',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='license',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='expiry',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='license',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='passport',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='passport',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='passport',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='permanentaddress',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='name',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='sbook',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sbook',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='sbook',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='schengenvisa',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='schengenvisa',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='schengenvisa',
            name='schengen_visa',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='schengenvisa',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='seaservice',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='seaservice',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='spouse',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='spouse',
            name='married_date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='spouse',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='src',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='src',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='src',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='trainingcertificates',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='trainingcertificates',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='usvisa',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usvisa',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='usvisa',
            name='us_visa',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='usvisa',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='yellowfever',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='yellowfever',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='yellowfever',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='essay',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appsource',
            name='source',
            field=models.ForeignKey(default=None, to='application_form.Sources'),
        ),
        migrations.AlterField(
            model_name='coc',
            name='coc',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='coc',
            name='expiry',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='coc',
            name='rank',
            field=models.ForeignKey(default=None, to='application_form.Rank'),
        ),
        migrations.AlterField(
            model_name='currentaddress',
            name='street',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='currentaddress',
            name='zip',
            field=models.ForeignKey(default=None, to='application_form.Zip'),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='contact',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='relationship',
            field=models.ForeignKey(default=None, to='application_form.Relationship'),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='street',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='zip',
            field=models.ForeignKey(default=None, to='application_form.Zip'),
        ),
        migrations.RemoveField(
            model_name='flagdocuments',
            name='flags',
        ),
        migrations.AlterField(
            model_name='goc',
            name='expiry',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='goc',
            name='goc',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='license',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='expiry',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='passport',
            name='passport',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='permanentaddress',
            name='street',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='permanentaddress',
            name='zip',
            field=models.ForeignKey(default=None, to='application_form.Zip'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='age',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='availability_date',
            field=django_date_extensions.fields.ApproximateDateField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='birth_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='birth_place',
            field=models.ForeignKey(default=None, to='application_form.BirthPlace'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='civil_status',
            field=models.ForeignKey(default=None, to='application_form.CivilStatus'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='email_address_1',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='father_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='landline_1',
            field=models.PositiveIntegerField(default=None, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{7})$', message=b'Please input proper 7 digit telephone number format')]),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='landline_2',
            field=models.PositiveIntegerField(default=None, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{7})$', message=b'Please input proper 7 digit telephone number format')]),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='mobile_1',
            field=models.BigIntegerField(default=None, null=True, validators=[django.core.validators.RegexValidator(regex=b'^09([0-9]{9})$', message=b'Please input proper mobile number format 09xxxxxxxxx')]),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='mobile_2',
            field=models.BigIntegerField(default=None, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^09([0-9]{9})$', message=b'Please input proper mobile number format 09xxxxxxxxx')]),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='mother_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='pagibig',
            field=models.BigIntegerField(default=None, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{12})$', message=b'Please input proper 12 digit format of pagibig')]),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='philhealth',
            field=models.BigIntegerField(default=None, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{12})$', message=b'Please input proper 12 digit format of philhealth')]),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='preferred_vessel_type',
            field=models.ForeignKey(default=None, to='application_form.VesselType'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='sss',
            field=models.PositiveIntegerField(default=None, null=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{10})$', message=b'Please input proper 10 digit format of sss')]),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='tin',
            field=models.BigIntegerField(default=None, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{12})$', message=b'Please input proper 12 digit format of tin')]),
        ),
        migrations.AlterField(
            model_name='sbook',
            name='expiry',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='sbook',
            name='sbook',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='schengenvisa',
            name='expiry',
            field=models.DateField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='cause_of_discharge',
            field=models.ForeignKey(default=None, to='application_form.CauseOfDischarge'),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='date_joined',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='date_left',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='duration',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='dwt',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='engine_type',
            field=models.ForeignKey(default=None, to='application_form.EngineType'),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='flag',
            field=models.ForeignKey(default=None, to='application_form.Flags'),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='grt',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='hp',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='kw',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='manning_agency',
            field=models.ForeignKey(default=None, to='application_form.ManningAgency'),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='principal',
            field=models.ForeignKey(default=None, to='application_form.Principal'),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='rank',
            field=models.ForeignKey(default=None, to='application_form.Rank'),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='vessel_name',
            field=models.ForeignKey(default=None, to='application_form.VesselName'),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='vessel_type',
            field=models.ForeignKey(default=None, to='application_form.VesselType'),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='year_built',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='birthdate',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='contact',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='src',
            name='rank',
            field=models.ForeignKey(default=None, to='application_form.Rank'),
        ),
        migrations.AlterField(
            model_name='src',
            name='src',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainingcertificates',
            name='trainings_certificates',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usvisa',
            name='expiry',
            field=models.DateField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='yellowfever',
            name='expiry',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='yellowfever',
            name='yellow_fever',
            field=models.CharField(default=None, max_length=100, unique=True, null=True),
        ),
        migrations.DeleteModel(
            name='AppDetails',
        ),
        migrations.DeleteModel(
            name='BackgroundInformation',
        ),
        migrations.DeleteModel(
            name='CertificatesDocuments',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Reference',
        ),
        migrations.AddField(
            model_name='trainingcertificatedocuments',
            name='trainings_certificates',
            field=models.ManyToManyField(default=None, to='application_form.TrainingCertificates'),
        ),
        migrations.AddField(
            model_name='trainingcertificatedocuments',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='disciplinaryaction',
            name='reason',
            field=models.ForeignKey(default=None, to='application_form.Reasons'),
        ),
        migrations.AddField(
            model_name='disciplinaryaction',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='detained',
            name='reason',
            field=models.ForeignKey(default=None, to='application_form.Reasons'),
        ),
        migrations.AddField(
            model_name='detained',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='appform',
            name='alternative_position',
            field=models.ForeignKey(related_name='alternative_position', default=None, to='application_form.Rank'),
        ),
        migrations.AddField(
            model_name='appform',
            name='position_applied',
            field=models.ForeignKey(related_name='position_applied', default=None, to='application_form.Rank'),
        ),
        migrations.AddField(
            model_name='appform',
            name='status',
            field=models.ForeignKey(default=None, to='application_form.Status'),
        ),
        migrations.AddField(
            model_name='appsource',
            name='specific',
            field=models.ForeignKey(default=None, to='application_form.Specifics'),
        ),
        migrations.AddField(
            model_name='college',
            name='college',
            field=models.ForeignKey(related_name='Colleges', default=None, to='application_form.Colleges'),
        ),
        migrations.AddField(
            model_name='college',
            name='degree',
            field=models.ForeignKey(default=None, to='application_form.Degree'),
        ),
        migrations.AddField(
            model_name='highschool',
            name='highschool',
            field=models.ForeignKey(related_name='Highschools', default=None, to='application_form.HighSchools'),
        ),
        migrations.AddField(
            model_name='flagdocuments',
            name='flags',
            field=models.ManyToManyField(default=None, to='application_form.Flags', blank=True),
        ),
    ]
