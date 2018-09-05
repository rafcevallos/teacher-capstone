from django.shortcuts import render
from readapi.views import login_user
from readapi.forms import UserForm, ProfileForm


def register(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':  # If we go to /register, this will load.
        profile_form = ProfileForm()
        user_form = UserForm()  # UserForm is from Django,
        # renders form
        return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})
        # {'user_form': user_form} <-- this contains the form objects
