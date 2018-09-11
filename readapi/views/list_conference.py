from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from readapi.models import ConferenceLog


@login_required
def list_conference(request):
    search_terms = request.GET.get('search_terms', '')
    all_conference = ConferenceLog.objects.all()
    if search_terms:
        search_results = [
            item for item in all_conference if search_terms in item.title]
        # filter all_conference and render the filtered stuff
        return render(request, 'conference/list_conference.html', {'conferences': search_results})
    else:
        return render(request, 'conference/list_conference.html', {'all_conference': all_conference})
