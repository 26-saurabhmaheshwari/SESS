from django import forms
from .models import lms_details

class lmsCreateForm(forms.ModelForm):
  class Meta:
    model = lms_details
    fields = '__all__'
    exclude = ['ls_status']
    widgets = {
       'ls_date': forms.TextInput(attrs={'type' : 'date','class': "form-control "}),
        'ls_reason' : forms.TextInput(attrs={ 'class': "form-control "}),
        }

class lmsViewForm(forms.ModelForm):
      class Meta:
            model = lms_details
            fields = '__all__'