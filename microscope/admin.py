from django.contrib import admin
from microscope.models import Slide

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slide, AuthorAdmin)
# Register your models here.
