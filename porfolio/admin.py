from django.contrib import admin
from .models import Project


# Register your models here.
# voy extender funionalidades del admin
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Project,ProjectAdmin)
