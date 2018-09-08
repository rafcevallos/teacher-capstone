from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import RequestContext
from readapi.models import Student
from readapi.forms import StudentForm


@login_required
def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            new_student = student_form.save()
            new_student.save()
            return redirect('readapi:list_students')
    else:
        student_form = StudentForm()
    return render(request, 'student/add_student.html', {'student_form': student_form})