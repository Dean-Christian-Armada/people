from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from . models import *

# Register your models here.
# class TrainingCertificatesResource(resources.ModelResource):
# 	class Meta:
# 		model = TrainingCertificates

# class TrainingCertificatesImport(ImportExportModelAdmin):
# 	resource_class = TrainingCertificatesResource

# class FlagsResource(resources.ModelResource):
# 	class Meta:
# 		model = Flags

# class FlagsImport(ImportExportModelAdmin):
# 	resource_class = FlagsResource

admin.site.register(ApplicationFormPersonalData)