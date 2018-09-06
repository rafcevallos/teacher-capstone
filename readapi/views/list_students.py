from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from readapi.models import Student

@login_required
def list_students(request):
    all_students = Student.objects.all()
    return render(request, 'student/list_student.html', {'all_students': all_students})