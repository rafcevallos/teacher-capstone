from django import forms
from readapi.models import User

class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)