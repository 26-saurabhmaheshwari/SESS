from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Employee
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field, HTML, MultiWidgetField, Fieldset


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        #fields = ['first_name','last_name']

        #first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
        #last_name = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password']

