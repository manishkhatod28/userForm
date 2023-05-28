from django import forms
from django.core.exceptions import ValidationError
from datetime import date

from userapp.models import UserForm


class UserFormForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise ValidationError('You must be at least 18 years old.')
        return dob

    class Meta:
        model = UserForm
        fields = '__all__'
