# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150902_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllotmentDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allottee_name', models.CharField(default=None, max_length=100)),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('contact_number', models.BigIntegerField()),
                ('account_number', models.BigIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(default=None, upload_to=b'application/pictures', blank=True)),
                ('signatures', models.ImageField(default=None, upload_to=b'application/signatures', blank=True)),
                ('application_date', models.DateField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('essay', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='AppSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bank', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('barangay', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BeneficiaryDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(default=None, max_length=30)),
                ('first_name', models.CharField(default=None, max_length=30)),
                ('middle_name', models.CharField(default=None, max_length=30)),
                ('contact_number', models.BigIntegerField()),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BirthPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth_place', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CauseOfDischarge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cause_of_discharge', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CivilStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('civil_status', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='COC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coc', models.CharField(default=None, unique=True, max_length=100)),
                ('issued', models.DateField(default=None)),
                ('expiry', models.DateField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schoolyear_from', models.PositiveSmallIntegerField(default=None)),
                ('schoolyear_to', models.PositiveSmallIntegerField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college', models.CharField(default=None, max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(default=None, max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detained',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detained', models.NullBooleanField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dialect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialect', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaryAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disciplinary_action', models.NullBooleanField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100)),
                ('contact', models.CharField(default=None, max_length=100)),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engine_type', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('english', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FlagDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlagDocumentsDetailed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sbook_number', models.PositiveIntegerField()),
                ('sbook_expiry', models.DateField()),
                ('license_number', models.PositiveIntegerField()),
                ('license_expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Flags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flags', models.CharField(default=None, max_length=50)),
                ('company_standard', models.NullBooleanField(default=False, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GOC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goc', models.CharField(default=None, unique=True, max_length=100)),
                ('issued', models.DateField(default=None)),
                ('expiry', models.DateField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schoolyear_from', models.PositiveSmallIntegerField(default=None)),
                ('schoolyear_to', models.PositiveSmallIntegerField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchools',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('highschool', models.CharField(default=None, max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LandEmployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer_name', models.CharField(default=None, max_length=100)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('contact_person', models.CharField(default=None, max_length=100)),
                ('contact_number', models.BigIntegerField()),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license', models.CharField(default=None, unique=True, max_length=100)),
                ('issued', models.DateField(default=None)),
                ('expiry', models.DateField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ManningAgency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manning_agency', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('municipality', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passport', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PassportPlaceIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_1', models.BigIntegerField(default=None, validators=[django.core.validators.RegexValidator(regex=b'^09([0-9]{9})$', message=b'Please input proper mobile number format 09xxxxxxxxx')])),
                ('mobile_2', models.BigIntegerField(default=None, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^09([0-9]{9})$', message=b'Please input proper mobile number format 09xxxxxxxxx')])),
                ('father_name', models.CharField(default=None, max_length=100)),
                ('mother_name', models.CharField(default=None, max_length=100)),
                ('age', models.PositiveIntegerField(default=None)),
                ('landline_1', models.PositiveIntegerField(default=None, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{7})$', message=b'Please input proper 7 digit telephone number format')])),
                ('landline_2', models.PositiveIntegerField(default=None, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{7})$', message=b'Please input proper 7 digit telephone number format')])),
                ('sss', models.PositiveIntegerField(default=None, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{10})$', message=b'Please input proper 10 digit format of sss')])),
                ('philhealth', models.BigIntegerField(default=None, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{12})$', message=b'Please input proper 12 digit format of philhealth')])),
                ('tin', models.BigIntegerField(default=None, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{12})$', message=b'Please input proper 12 digit format of tin')])),
                ('pagibig', models.BigIntegerField(default=None, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{12})$', message=b'Please input proper 12 digit format of pagibig')])),
                ('email_address_1', models.EmailField(default=None, max_length=254)),
                ('email_address_2', models.EmailField(default=None, max_length=254, blank=True)),
                ('birth_date', models.DateField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('availability_date', django_date_extensions.fields.ApproximateDateField(default=None, max_length=10)),
                ('birth_place', models.ForeignKey(default=None, to='mariners_profile.BirthPlace')),
                ('civil_status', models.ForeignKey(default=None, to='mariners_profile.CivilStatus')),
                ('current_address', models.ForeignKey(default=None, to='mariners_profile.CurrentAddress')),
                ('dialect', models.ForeignKey(default=None, blank=True, to='mariners_profile.Dialect')),
                ('english', models.ForeignKey(default=None, blank=True, to='mariners_profile.English')),
                ('name', models.OneToOneField(default=None, to='login.UserProfile')),
                ('permanent_address', models.ForeignKey(default=None, to='mariners_profile.PermanentAddress')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('principal', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reasons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField(default=None, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationship', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sbook', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SBookPlaceIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SchengenVisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schengen_visa', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField(default=None, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='SeaService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grt', models.PositiveIntegerField(default=None)),
                ('dwt', models.PositiveIntegerField(default=None)),
                ('year_built', models.PositiveSmallIntegerField(default=None)),
                ('duration', models.PositiveSmallIntegerField(default=None)),
                ('hp', models.DecimalField(default=None, max_digits=10, decimal_places=1)),
                ('kw', models.DecimalField(default=None, max_digits=10, decimal_places=1)),
                ('date_joined', models.DateField(default=None)),
                ('date_left', models.DateField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('cause_of_discharge', models.ForeignKey(default=None, to='mariners_profile.CauseOfDischarge')),
                ('engine_type', models.ForeignKey(default=None, to='mariners_profile.EngineType')),
                ('flag', models.ForeignKey(default=None, to='mariners_profile.Flags')),
                ('manning_agency', models.ForeignKey(default=None, to='mariners_profile.ManningAgency')),
                ('principal', models.ForeignKey(default=None, to='mariners_profile.Principal')),
                ('rank', models.ForeignKey(default=None, to='mariners_profile.Rank')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specifics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specific', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100, blank=True)),
                ('married_date', models.DateField(default=None, blank=True)),
                ('birthdate', models.DateField(default=None, blank=True)),
                ('contact', models.CharField(default=None, max_length=100, blank=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='SRC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('src', models.CharField(default=None, unique=True, max_length=100)),
                ('issued', models.DateField(default=None)),
                ('expiry', models.DateField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('rank', models.ForeignKey(default=None, to='mariners_profile.Rank')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='STCWCertificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issued', models.DateField(default=None)),
                ('expiry', models.DateField(default=None)),
                ('rank', models.ForeignKey(default=None, to='mariners_profile.Rank')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='STCWEndorsement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issued', models.DateField(default=None)),
                ('expiry', models.DateField(default=None)),
                ('rank', models.ForeignKey(default=None, to='mariners_profile.Rank')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('training_center', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCertificateDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCertificateDocumentsDetailed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField()),
                ('issued', models.DateField()),
                ('place_trained', models.OneToOneField(to='mariners_profile.TrainingCenter')),
                ('trainings_certificate_documents', models.ForeignKey(to='mariners_profile.TrainingCertificateDocuments')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCertificates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trainings_certificates', models.CharField(default=None, max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='USVisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('us_visa', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField(default=None, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='VesselName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vessel_name', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VesselType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vessel_type', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisaApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visa_application', models.NullBooleanField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('reason', models.ForeignKey(default=None, to='mariners_profile.Reasons')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='YellowFever',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yellow_fever', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.PositiveIntegerField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('barangay', models.ForeignKey(default=None, to='mariners_profile.Barangay')),
                ('municipality', models.ForeignKey(default=None, to='mariners_profile.Municipality')),
            ],
        ),
        migrations.AddField(
            model_name='trainingcertificatedocuments',
            name='trainings_certificates',
            field=models.ManyToManyField(default=None, to='mariners_profile.TrainingCertificates'),
        ),
        migrations.AddField(
            model_name='trainingcertificatedocuments',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='seaservice',
            name='vessel_name',
            field=models.ForeignKey(default=None, to='mariners_profile.VesselName'),
        ),
        migrations.AddField(
            model_name='seaservice',
            name='vessel_type',
            field=models.ForeignKey(default=None, to='mariners_profile.VesselType'),
        ),
        migrations.AddField(
            model_name='sbook',
            name='place_issued',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.SBookPlaceIssued'),
        ),
        migrations.AddField(
            model_name='sbook',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='preferred_vessel_type',
            field=models.ForeignKey(default=None, to='mariners_profile.VesselType'),
        ),
        migrations.AddField(
            model_name='permanentaddress',
            name='zip',
            field=models.ForeignKey(default=None, to='mariners_profile.Zip'),
        ),
        migrations.AddField(
            model_name='passport',
            name='place_issued',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.PassportPlaceIssued'),
        ),
        migrations.AddField(
            model_name='passport',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='landemployment',
            name='position',
            field=models.ForeignKey(default=None, to='mariners_profile.Position'),
        ),
        migrations.AddField(
            model_name='landemployment',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='landemployment',
            name='zip',
            field=models.ForeignKey(default=None, to='mariners_profile.Zip'),
        ),
        migrations.AddField(
            model_name='highschool',
            name='highschool',
            field=models.ForeignKey(related_name='Highschools', default=None, to='mariners_profile.HighSchools'),
        ),
        migrations.AddField(
            model_name='highschool',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='flagdocumentsdetailed',
            name='flags',
            field=models.ForeignKey(to='mariners_profile.Flags'),
        ),
        migrations.AddField(
            model_name='flagdocumentsdetailed',
            name='flags_documents',
            field=models.ForeignKey(to='mariners_profile.FlagDocuments'),
        ),
        migrations.AddField(
            model_name='flagdocuments',
            name='flags',
            field=models.ManyToManyField(default=None, to='mariners_profile.Flags', through='mariners_profile.FlagDocumentsDetailed', blank=True),
        ),
        migrations.AddField(
            model_name='flagdocuments',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='relationship',
            field=models.ForeignKey(default=None, to='mariners_profile.Relationship'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='zip',
            field=models.ForeignKey(default=None, to='mariners_profile.Zip'),
        ),
        migrations.AddField(
            model_name='disciplinaryaction',
            name='reason',
            field=models.ForeignKey(default=None, to='mariners_profile.Reasons'),
        ),
        migrations.AddField(
            model_name='disciplinaryaction',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='detained',
            name='reason',
            field=models.ForeignKey(default=None, to='mariners_profile.Reasons'),
        ),
        migrations.AddField(
            model_name='detained',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='currentaddress',
            name='zip',
            field=models.ForeignKey(default=None, to='mariners_profile.Zip'),
        ),
        migrations.AddField(
            model_name='college',
            name='college',
            field=models.ForeignKey(related_name='Colleges', default=None, to='mariners_profile.Colleges'),
        ),
        migrations.AddField(
            model_name='college',
            name='degree',
            field=models.ForeignKey(default=None, to='mariners_profile.Degree'),
        ),
        migrations.AddField(
            model_name='college',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='coc',
            name='rank',
            field=models.ForeignKey(default=None, to='mariners_profile.Rank'),
        ),
        migrations.AddField(
            model_name='coc',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='beneficiarydetails',
            name='relationship',
            field=models.ForeignKey(default=None, to='mariners_profile.Relationship'),
        ),
        migrations.AddField(
            model_name='beneficiarydetails',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='beneficiarydetails',
            name='zip',
            field=models.ForeignKey(default=None, to='mariners_profile.Zip'),
        ),
        migrations.AddField(
            model_name='appsource',
            name='source',
            field=models.ForeignKey(default=None, to='mariners_profile.Sources'),
        ),
        migrations.AddField(
            model_name='appsource',
            name='specific',
            field=models.ForeignKey(default=None, to='mariners_profile.Specifics'),
        ),
        migrations.AddField(
            model_name='appform',
            name='alternative_position',
            field=models.ForeignKey(related_name='alternative_position', default=None, to='mariners_profile.Rank'),
        ),
        migrations.AddField(
            model_name='appform',
            name='application_source',
            field=models.ForeignKey(default=None, to='mariners_profile.AppSource'),
        ),
        migrations.AddField(
            model_name='appform',
            name='position_applied',
            field=models.ForeignKey(related_name='position_applied', default=None, to='mariners_profile.Rank'),
        ),
        migrations.AddField(
            model_name='appform',
            name='status',
            field=models.ForeignKey(default=None, to='mariners_profile.Status'),
        ),
        migrations.AddField(
            model_name='appform',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='allotmentdetails',
            name='bank',
            field=models.ForeignKey(default=None, to='mariners_profile.Bank'),
        ),
        migrations.AddField(
            model_name='allotmentdetails',
            name='branch',
            field=models.ForeignKey(default=None, to='mariners_profile.Branch'),
        ),
        migrations.AddField(
            model_name='allotmentdetails',
            name='relationship',
            field=models.ForeignKey(default=None, to='mariners_profile.Relationship'),
        ),
        migrations.AddField(
            model_name='allotmentdetails',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='allotmentdetails',
            name='zip',
            field=models.ForeignKey(default=None, to='mariners_profile.Zip'),
        ),
    ]
