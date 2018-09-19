from django import forms
from readapi.models import Student, User


class StudentForm(forms.ModelForm):
    # teacher = forms.ModelChoiceField(
    #     queryset=Student.objects.filter(teacher="teacher"),
    #     empty_label="(Select Teacher)",
    #     label="",
    #     required=True,
    #     widget=TeacherSelect(
    #         attrs={'value': ''}
    #     )
    # )

    # first_name = forms.CharField(
    #     label="",
    #     max_length=50,
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={'class': 'input is-focused', 'type': "text",
    #                'placeholder': '{{student_form.first_name}}'}
    #     )
    # )

    # last_name = forms.CharField(
    #     label="",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={'class': 'input is-focused', 'type': "text",
    #                'placeholder': '{{student_form.last_name}}'}
    #     )
    # )

    # notes = forms.CharField(
    #     label="",
    #     required=True,
    #     widget=forms.Textarea(
    #         attrs={'class': 'textarea is-focused', 'type': "text",
    #                'placeholder': '{{student_form.notes}}'}
    #     )
    # )

    class Meta:
        model = Student
        fields = '__all__'
