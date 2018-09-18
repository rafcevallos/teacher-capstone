from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from readapi.models import Student


@login_required
def index(request):
    # All students in database will be listed on the index/home page
    # Gets user search input from navbar
    search_terms = request.GET.get('search_terms', '')
    # Turns user search input to all lowercase
    lower_search_terms = search_terms.lower()
    print('Search Terms:', search_terms)
    # we need to filter the students by user ID otherwise you will continue to get EVERY student in the DB
    all_students = Student.objects.filter(teacher_id=request.user)
    if search_terms:
        search_results = [
            level for level in all_students if lower_search_terms in level.reading_level.lower()
        ]  # gets the reading level for students in the queryset
        return render(request, 'student/search_student.html', {'search_results': search_results})
    else:
        return render(request, 'index.html', {'all_students': all_students})
