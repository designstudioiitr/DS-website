# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Projects(models.Model) :
    sno = models.IntegerField(help_text="Enter 0 for first project", default = 0)
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255, help_text="Field needs to be unique")
    text_color = models.CharField(max_length=10, help_text="Enter Hex Code, eg #ffffff")
    color = models.CharField(max_length=10, help_text="Enter Hex Code, eg #ffffff")
    end_color = models.CharField(max_length=10, help_text="Enter Hex Code, eg #ffffff")
    subhead = models.CharField(max_length=1000)
    brief = models.CharField(max_length=1000)
    about = models.CharField(max_length=5000)
    idea = models.CharField(max_length=5000)
    details = models.CharField(max_length=5000)

    def __unicode__(self) :
        return "%s-%s-%s-%s-%s-%s-%s-%s-%s-%s-%s" % (self.sno, self.name, self.identifier, self.text_color, self.subhead, self.color, self.end_color, self.brief, self.about, self.idea, self.details)
