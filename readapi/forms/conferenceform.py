from django import forms
from readapi.models import ConferenceLog, Strategy, Observation


class ConferenceForm(forms.ModelForm):
    # Strategy and Observation are foreign keys on the ConferenceLog model, so we want to turn the items in each as checkboxes
    strategy = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Strategy.objects.all())

    observation = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Observation.objects.all())

    class Meta:
        model = ConferenceLog
        fields = '__all__'