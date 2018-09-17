from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from readapi.models import Student


@login_required
def index(request):
    # All students in database will be listed on the index/home page
    all_students = Student.objects.filter(teacher_id=request.user) #we need to filter the students by user ID otherwise you will continue to get EVERY student in the DB
    return render(request, 'index.html', {'all_students': all_students})