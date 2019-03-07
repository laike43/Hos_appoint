from django.contrib import admin

from client.models import Patient,Appointment
# Register your models here.

admin.site.register(Patient)
admin.site.register(Appointment)