from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from readapi.models import Student


@login_required
def index(request):
    # All students in database will be listed on the index/home page
    search_terms = request.GET.get('search_terms', '')
    print(search_terms)
    all_students = Student.objects.filter(teacher_id=request.user) #we need to filter the students by user ID otherwise you will continue to get EVERY student in the DB
    if search_terms.lower():
        search_results = [
            student for student in all_students if search_terms in student.first_name.lower()
        ]
        return render(request, 'student/search_student.html', {'search_results': search_results})
    else:
        return render(request, 'index.html', {'all_students': all_students})
