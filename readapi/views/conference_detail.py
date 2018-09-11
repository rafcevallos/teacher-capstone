from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from readapi.models import ConferenceLog


@login_required
def conference_detail(request, pk):
    """
    View manages the conference log detail from the conference list view
    """
    if request.method == 'GET':
        conference = ConferenceLog.objects.get(pk=pk)
        return render(request, 'conference/detail_conference.html', {'conference': conference})