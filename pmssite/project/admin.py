from django.contrib import admin
from .models import Project, Task


# Registering models Project and Task
admin.site.register(Project)
admin.site.register(Task)
