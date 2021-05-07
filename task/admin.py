from django.contrib import admin
from .models import Playbook, Job


# Register your models here.

class PlaybookAdmin(admin.ModelAdmin):
    pass


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(Playbook, PlaybookAdmin)
admin.site.register(Job, JobAdmin)
