from django.contrib import admin
from . models import *

# Register your models here.

class SeaServiceInline(admin.TabularInline):
	model = SeaService

class FlagDocumentsInline(admin.TabularInline):
	model = FlagDocuments

class TrainingCertificatesInline(admin.TabularInline):
	model = TrainingCertificates

class AppFormAdmin(admin.ModelAdmin):
	inlines = [
		SeaServiceInline
	]

admin.site.register(AppDetails)
admin.site.register(AppSource)
admin.site.register(Tertiary)
admin.site.register(HighSchool)
admin.site.register(Education)
admin.site.register(EmergencyContact)
admin.site.register(SeaService)
admin.site.register(BackgroundInformation)
admin.site.register(Passport)
admin.site.register(SBook)
admin.site.register(COC)
admin.site.register(License)
admin.site.register(SRC)
admin.site.register(GOC)
admin.site.register(USVisa)
admin.site.register(SchengenVisa)
admin.site.register(YellowFever)
admin.site.register(CertificatesDocuments)
admin.site.register(FlagDocuments)
admin.site.register(TrainingCertificates)
admin.site.register(PersonalData)
admin.site.register(AppForm, AppFormAdmin)
admin.site.register(Reference)
# admin.site.register(JSignatureModel)
# admin.site.register(Sample)