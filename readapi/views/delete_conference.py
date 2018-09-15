from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.template import RequestContext
from readapi.models import ConferenceLog


@login_required
def delete_conference(request, pk):
    """Displays template for deleting a conference log"""
    conference = ConferenceLog.objects.get(pk=pk)
    conference.delete()
    return redirect('readapi:index')
