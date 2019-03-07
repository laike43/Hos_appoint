from django.contrib import admin

from comapp.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('column','title','author','pub_date','update_time')

admin.site.register(Blog,BlogAdmin)