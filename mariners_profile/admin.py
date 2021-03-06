from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

# from .models import Flags, TrainingCertificates, Colleges, Degree, HighSchools, Barangay, Municipality, Relationship, Sources, Specifics, Reasons, Rank, BirthPlace, VesselType, CivilStatus, VesselName, EngineType, ManningAgency, Principal, CauseOfDischarge, Status, Zip

from .models import *

# Register your models here.

class TrainingCertificatesResource(resources.ModelResource):
	class Meta:
		model = TrainingCertificates

class TrainingCertificatesImport(ImportExportModelAdmin):
	resource_class = TrainingCertificatesResource

class ReferrersPoolResource(resources.ModelResource):
	class Meta:
		model = ReferrersPool

class ReferrersPoolImport(ImportExportModelAdmin):
	resource_class = ReferrersPoolResource

admin.site.register(Zip)
admin.site.register(CurrentAddress)
admin.site.register(PermanentAddress)
admin.site.register(CivilStatus)
admin.site.register(PersonalData)
admin.site.register(Spouse)
admin.site.register(Colleges)
admin.site.register(Degree)
admin.site.register(College)
admin.site.register(HighSchools)
admin.site.register(HighSchool)
admin.site.register(EmergencyContact)
admin.site.register(Barangay)
admin.site.register(Municipality)
admin.site.register(Relationship)
admin.site.register(VisaApplication)
admin.site.register(Detained)
admin.site.register(DisciplinaryAction)
admin.site.register(ChargedOffense)
admin.site.register(Termination)
admin.site.register(Passport)
admin.site.register(Sources)
admin.site.register(Specifics)
admin.site.register(Reasons)
admin.site.register(Rank)
admin.site.register(BirthPlace)
# admin.site.register(VesselType)
# admin.site.register(CivilStatus)
# admin.site.register(VesselName)
# admin.site.register(EngineType)
# admin.site.register(ManningAgency)
# admin.site.register(Principal)
admin.site.register(CauseOfDischarge)
# admin.site.register(Status)
# admin.site.register(Zip)
admin.site.register(SeaService)
admin.site.register(Sbook)
admin.site.register(COC)
admin.site.register(License)
admin.site.register(SRC)
admin.site.register(GOC)
admin.site.register(USVisa)
admin.site.register(SchengenVisa)
admin.site.register(YellowFever)
admin.site.register(Flags)
admin.site.register(FlagDocuments)
admin.site.register(FlagDocumentsDetailed)
admin.site.register(TrainingCenter)
admin.site.register(TrainingCertificatesSegregation)
admin.site.register(TrainingCertificates, TrainingCertificatesImport)
admin.site.register(TrainingCertificateDocuments)
admin.site.register(TrainingCertificateDocumentsDetailed)
admin.site.register(ReferrersPool, ReferrersPoolImport)
admin.site.register(Status)
admin.site.register(MarinersProfile)