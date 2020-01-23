from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    CHOICES = [('D', 'Doctor'),
               ('P', 'Patient')]
    account_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    specialization = forms.CharField(help_text='')

    class Meta:
        model = User
        fields = ('username', 'account_type', 'specialization', 'password1', 'password2', )