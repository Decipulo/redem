from django.forms import ModelForm
from django import forms
from .models import login, Applicant, Account

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            "User",
            "disability",
            "Address",
            "Age",
            "ContactNumber",
            "Avatar",
            ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = [
            "Username",
            "Email",
            "password",
            ]




