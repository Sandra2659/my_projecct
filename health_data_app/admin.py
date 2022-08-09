from django.contrib import admin
from .models import *

from health_data_app import models

admin.site.register(models.Login)
admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.Specialist)
admin.site.register(models.Report)
admin.site.register(models.drsharedata)
admin.site.register(models.spsharedata)
admin.site.register(models.Complaint)
admin.site.register(models.Prescription)
admin.site.register(models.Refer)
admin.site.register(models.drsharereport)
