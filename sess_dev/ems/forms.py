from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext as _

# from .models import Employee

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'date_joined']
        # username.help_text = ''
        labels = {
           'is_staff': "Staff privilege",
           
        }
       
        # username.help_text = ''

        # fields['username'].help_text = None
        widgets = {
            'username': forms.TextInput(attrs={ 'class': "form-control "}),
            'first_name' : forms.TextInput(attrs={ 'class': "form-control "}),
            'last_name' : forms.TextInput(attrs={'class': "form-control  "}),
            'email' : forms.TextInput(attrs={'type' : 'email','class': "form-control "}),
            'password' : forms.TextInput(attrs={'type' : 'password','class': "form-control "}),
            'is_staff' : forms.CheckboxInput(attrs={'class': "checkbox "}),
            'date_joined' : forms.TextInput(attrs={'type' : 'date','class': "form-control "})
            
        }
        help_texts = {
            'username': _(''),
            'is_staff': _(''),
            'is_active': _(' '),
            
        }