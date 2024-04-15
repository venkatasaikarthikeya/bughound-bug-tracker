from django.contrib import admin

# Register your models here.

from .models import Program, FunctionalArea

admin.site.register(Program)
admin.site.register(FunctionalArea)