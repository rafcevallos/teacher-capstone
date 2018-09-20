from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.urls import reverse
from readapi.forms import ConferenceForm
from readapi.models import ConferenceLog


@login_required
def edit_conference(request, pk):
    print(pk)
    if request.method == "GET":
        print("GET")
        conference = ConferenceLog.objects.get(pk=pk)
        print('Thing', conference)
        # Here's where we load the form with the fields and data from the DB
        conference_form = ConferenceForm(initial={
            'student': conference.student,
            'book': conference.book,
            'strategy': conference.strategy.all, # How to target many to many field join table data
            'observation': conference.observation.all,  # How to target many to many field join table data
            'reading_level': conference.reading_level,
            'comments': conference.comments
            })
        return render(request, 'conference/edit_conference.html', {'conference': conference, 'conference_form': conference_form})

    elif request.method == "POST":
        print("POST")
        # Here's where we post upstudent,d info to the conference
        conference = ConferenceLog.objects.get(pk=pk)
        conference_form = ConferenceForm(
            request.POST, instance=conference)
        print('HERE IS THE STRING')

        if conference_form.is_valid():
            conference_form.save()

            return redirect(reverse('readapi:student_detail', args=(conference.student.id,)))
            # args expects a tuple of values that are iterable.  Without a comma, it won't register it as a tuple
