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

class lmsApproveForm(forms.ModelForm):
      emp_name = forms.CharField( initial="sau")
      class Meta:
            model = lms_details
            fields = '__all__'


class lmsViewForm(forms.ModelForm):
      class Meta:
            model = lms_details
            fields = '__all__'
            
class lmsUpdateForm(forms.ModelForm):
      class Meta:
            model = lms_details
            fields = ['ls_reason']
            widgets = {
                  'ls_reason' : forms.TextInput(attrs={ 'class': "form-control "})
        }



