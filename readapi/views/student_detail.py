from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from readapi.models import Student, ConferenceLog


@login_required
def student_detail(request, pk):
    """
    View manages the student detail from the student list view
    """
    if request.method == 'GET':
        student = Student.objects.get(pk=pk)
        all_conference = ConferenceLog.objects.all()
        return render(request, 'student/detail_student.html', {'student': student, 'all_conference': all_conference})