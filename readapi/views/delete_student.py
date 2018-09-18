from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.template import RequestContext
from readapi.models import Student

@login_required
def delete_student(request, pk):
    """Displays template for deleting a student"""
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('readapi:index')