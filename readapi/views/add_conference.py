from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import RequestContext
from readapi.models import ConferenceLog
from readapi.forms import ConferenceForm


@login_required
def add_conference(request):
    if request.method == 'POST':
        conference_form = ConferenceForm(request.POST, request.FILES)

        if conference_form.is_valid():
            new_conference = conference_form.save()
            new_conference.save()
            return redirect('readapi:index')
    else:
        conference_form = ConferenceForm()
    return render(request, 'conference/add_conference.html', {'conference_form': conference_form})