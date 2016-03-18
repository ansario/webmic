from django.contrib import admin
from microscope.models import Slide, Marker

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slide, AuthorAdmin)
admin.site.register(Marker, AuthorAdmin)
# Register your models here.
