from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.urls import reverse
from readapi.forms import ConferenceForm
from readapi.models import ConferenceLog


@login_required
def edit_conference(request, pk):
    print(pk)
    print(request.method)
    if request.method == "GET":
        print("GET")
        conference = ConferenceLog.objects.get(pk=pk)
        # Here's where we load the form
        conference_form = ConferenceForm(initial={'date': conference.date,
                                                  'student': conference.student, 'book': conference.book, 'strategy': conference.strategy, 'observation': conference.observation, 'reading_level': conference.reading_level, 'comments': conference.comments}, )  # create profile fields and set defaults)
        return render(request, 'conference/edit_conference.html', {'conference': conference, 'conference_form': conference_form})

    elif request.method == "POST":
        print("POST")
        # Here's where we post updated info to the user
        conference = ConferenceLog.objects.get(pk=pk)
        conference_form = ConferenceForm(request.POST, instance=conference)
        print('HERE IS THE STRING')

        if conference_form.is_valid():
            conference_form.save()

            return redirect(reverse('readapi:list_conference'))
