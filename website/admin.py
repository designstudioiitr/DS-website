# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Projects

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin) :
    list_display = ('sno', 'name', 'identifier', 'subhead', 'text_color', 'color', 'end_color', 'brief', 'about', 'idea', 'details',)


admin.site.register(Projects, ProjectsAdmin)
