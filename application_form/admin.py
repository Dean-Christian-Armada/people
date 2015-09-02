from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from . models import *

# Register your models here.
class TrainingCertificatesResource(resources.ModelResource):
	class Meta:
		model = TrainingCertificates

class TrainingCertificatesImport(ImportExportModelAdmin):
	resource_class = TrainingCertificatesResource

class FlagsResource(resources.ModelResource):
	class Meta:
		model = Flags

class FlagsImport(ImportExportModelAdmin):
	resource_class = FlagsResource

admin.site.register(Flags, FlagsImport)
admin.site.register(TrainingCertificates, TrainingCertificatesImport)
admin.site.register(BirthPlace)
admin.site.register(VesselName)
admin.site.register(VesselType)
admin.site.register(Principal)
admin.site.register(CivilStatus)
admin.site.register(College)
admin.site.register(Degree)
admin.site.register(HighSchool)
admin.site.register(Relationship)
admin.site.register(Rank)
admin.site.register(EngineType)
admin.site.register(ManningAgency)
admin.site.register(CauseOfDischarge)
admin.site.register(Municipality)
admin.site.register(Barangay)
admin.site.register(Sources)
admin.site.register(Specifics)
admin.site.register(Reasons)
admin.site.register(Status)
admin.site.register(Spouse)
admin.site.register(Colleges)
admin.site.register(HighSchools)
admin.site.register(Zip)
admin.site.register(EmergencyContact)
admin.site.register(CurrentAddress)
admin.site.register(PermanentAddress)
admin.site.register(AppSource)
admin.site.register(VisaApplication)
admin.site.register(Detained)
admin.site.register(DisciplinaryAction)
admin.site.register(Passport)
admin.site.register(Sbook)
admin.site.register(COC)
admin.site.register(License)
admin.site.register(SRC)
admin.site.register(GOC)
admin.site.register(USVisa)
admin.site.register(SchengenVisa)
admin.site.register(YellowFever)
admin.site.register(PersonalData)
admin.site.register(SeaService)
admin.site.register(AppForm)
