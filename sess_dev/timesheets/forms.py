from django import forms
from .models import TimeRecords
from django.core.validators import MinLengthValidator


class CreateTimeSheetForm(forms.ModelForm):     
            
    emp_id = forms.IntegerField(widget=forms.HiddenInput(), initial=123) 

    class Meta:
        model = TimeRecords
        fields = '__all__'
        exclude = ['ts_status']
        labels = {
        "ts_desc": "Task Description"
            }
        widgets = {
        'ts_date': forms.TextInput(attrs={'readonly': True}),
        }
