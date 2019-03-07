from django.contrib import admin
from infirmary.models import Hospital,Department,Hospital_Department

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Hospital_Department)