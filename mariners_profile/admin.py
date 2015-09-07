from django.contrib import admin

# from .models import Flags, TrainingCertificates, Colleges, Degree, HighSchools, Barangay, Municipality, Relationship, Sources, Specifics, Reasons, Rank, BirthPlace, VesselType, CivilStatus, VesselName, EngineType, ManningAgency, Principal, CauseOfDischarge, Status, Zip

from .models import *

# Register your models here.

admin.site.register(Zip)
admin.site.register(CurrentAddress)
admin.site.register(PermanentAddress)
admin.site.register(CivilStatus)
admin.site.register(PersonalData)
admin.site.register(Spouse)
# admin.site.register(Flags)
# admin.site.register(TrainingCertificates)
admin.site.register(Colleges)
admin.site.register(Degree)
admin.site.register(College)
admin.site.register(HighSchools)
admin.site.register(HighSchool)
admin.site.register(EmergencyContact)
admin.site.register(Barangay)
admin.site.register(Municipality)
admin.site.register(Relationship)
# admin.site.register(Sources)
# admin.site.register(Specifics)
# admin.site.register(Reasons)
# admin.site.register(Rank)
admin.site.register(BirthPlace)
# admin.site.register(VesselType)
# admin.site.register(CivilStatus)
# admin.site.register(VesselName)
# admin.site.register(EngineType)
# admin.site.register(ManningAgency)
# admin.site.register(Principal)
# admin.site.register(CauseOfDischarge)
# admin.site.register(Status)
# admin.site.register(Zip)