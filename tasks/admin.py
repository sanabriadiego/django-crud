from django.contrib import admin
from .models import Task

#esta clase nos sirve para poder visualizar el campo "created" en el panel admin
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Task, TaskAdmin)
