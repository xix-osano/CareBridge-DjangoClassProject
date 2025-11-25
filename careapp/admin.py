from django.contrib import admin
from careapp.models import Patient, MedicalRecord, Appointment

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)