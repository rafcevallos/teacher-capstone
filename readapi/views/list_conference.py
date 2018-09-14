from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from readapi.models import ConferenceLog


@login_required
def list_conference(request):
    all_conference = ConferenceLog.objects.all()
    return render(request, 'conference/list_conference.html', {'all_conference': all_conference})
