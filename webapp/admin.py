from django.contrib import admin

# Register your models here.

from .models import Program, FunctionalArea, Employee, BugReport

admin.site.register(Program)
admin.site.register(FunctionalArea)
admin.site.register(Employee)
admin.site.register(BugReport)