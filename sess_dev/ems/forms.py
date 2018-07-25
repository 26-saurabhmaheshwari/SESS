from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
# from .models import Employee

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'date_joined']