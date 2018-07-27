from django import forms
from .models import TimeRecords
from django.core.validators import MinLengthValidator
from django.forms.widgets import SelectDateWidget


class CreateTimeSheetForm(forms.ModelForm):     
            
    # emp_id = forms.IntegerField(widget=forms.HiddenInput(), initial=123) ,
    # ts_start_date = forms.DateField(widget=extras.SelectDateWidget)
    # ts_start_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
    class Meta:
        model = TimeRecords
        fields = '__all__'
        exclude = ['ts_status']
        labels = {
        "ts_desc": "Task Description"
            }
        widgets = {
       'ts_date': forms.TextInput(attrs={'readonly': True}),
       'ts_date': forms.DateInput(attrs={'class':'datepicker'}),
        'ts_start_date': forms.DateInput(attrs={'id':'from', 'name':'start_date'}),

        }
