# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
from .mailing import send_mail

# Create your views here.
def index(request) :

    return render(request, 'index.html', {})

def contact(request) :

    return render(request, 'contact.html', {})

def portfolio(request) :
    data = Projects.objects.get(sno = 0)

    context = {
        "name" : data.name,
        "brief" : data.brief,
        "identifier" : data.identifier,
        "color" : data.color,
        "end_color" : data.end_color,
        "subhead" : data.subhead,
    }
    return render(request, 'portfolio.html', context)

def content_updater(request) :

    projects = Projects.objects.all().order_by('sno')
    content = []
    for project in projects :
        content.append(json.dumps({
            "name" : project.name,
            "subhead" : project.subhead,
            "brief" : project.brief,
            "color" : project.color,
            "identifier" : project.identifier,
            "end_color" : project.end_color,
        }))

    return HttpResponse(json.dumps(content), content_type='application/json')

def form_submit(request) :

    data = request.POST
    name = data.get('name')
    email = data.get('e-mail')
    message = data.get('message')

    subject = name + ' (' + email + ')'

    resp = {}

    try :
        send_mail(subject, message)
        resp = json.dumps({'status' : 200})
    except :
        resp = json.dumps({'status' : 404})

    return HttpResponse(resp, content_type='application/json')

def projects(request) :
    try :
        project = request.GET.get('name');
        data = Projects.objects.get(identifier = project)

        context = {
            "no" : data.sno,
            "name" : data.name,
            "brief" : data.brief,
            "text_color" : data.text_color,
            "color" : data.color,
            "end_color" : data.end_color,
            "subhead" : data.subhead,
            "about" : data.about,
            "details" : data.details,
            "idea" : data.idea,
            "identifier" : data.identifier,
        }

        return render(request, 'projects.html', context)

    except :
        project = request.GET.get('sno')
        num = len(Projects.objects.all())
        data = Projects.objects.get(sno = int(project)%num)

        context = {
            "no" : data.sno,
            "name" : data.name,
            "brief" : data.brief,
            "color" : data.color,
            "end_color" : data.end_color,
            "text_color" : data.text_color,
            "subhead" : data.subhead,
            "about" : data.about,
            "details" : data.details,
            "idea" : data.idea,
            "identifier" : data.identifier,
        }

        return render(request, 'projects.html', context)

def mobile(request) :
    return render(request, 'mobile.html', {})

def recruitment(request) :
    return render(request, 'portal.html', {})
