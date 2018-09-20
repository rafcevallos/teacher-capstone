from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.urls import reverse
from readapi.forms import StudentForm
from readapi.models import Student


@login_required
def edit_student(request, pk):
    print(pk)
    print(request.method)
    if request.method == "GET":
        print("GET")
        s = Student.objects.get(pk=pk)
        # Here's where we load the form
        student_form = StudentForm(initial={
            'first_name': s.first_name,
            'last_name': s.last_name,
            'photo': s.student_photo,
            'reading_level': s.reading_level,
            'skills': s.skills,
            'notes': s.notes},)  # create student fields and set defaults
        return render(request, 'student/edit_student.html', {'s': s, 'student_form': student_form})

    elif request.method == "POST":
        print("POST")
        # Here's where we post updated info to the user
        s = Student.objects.get(pk=pk)
        student_form = StudentForm(request.POST, instance=s)
        print('HERE IS THE STRING')

        if student_form.is_valid():
            student_form.save()

            return redirect(reverse('readapi:student_detail', args=(s.id,)))
