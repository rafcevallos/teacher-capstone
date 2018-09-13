from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from readapi.models import Skill


@login_required
def list_skill(request, pk):
    if request.method == 'GET':
        skills = Skill.objects.filter(reading_level=pk) # can filter on any object/context to find the property I need
        return render(request, 'skill/list_skill.html', {'skills': skills})
