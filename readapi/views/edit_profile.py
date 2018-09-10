from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from readapi.forms import ProfileForm, UserEditForm
from readapi.models import Profile


@login_required
def edit_profile(request):
    if request.method == "GET":
        u = User.objects.get(id=request.user.id)
        # Here's where we load the form
        user_form = UserEditForm(initial={'first_name': request.user.first_name,
                                          'last_name': request.user.last_name},)  # create user field and set defaults from currently signed in user
        profile_form = ProfileForm(initial={'address': u.profile.address,
                                            'phone': u.profile.phone},)  # create profile fields and set defaults. NEED TO MAKE THESE
        return render(request, 'edit_profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
        })

    elif request.method == "POST":
        # Here's where we post updated info to the user
        u = User.objects.get(id=request.user.id)
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=u.profile)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect(reverse('readapi:profile'))
