from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from .forms import CreateTimeSheetForm
from django.forms import formset_factory

# Create your views here. from sess_dev.timesheets.models import TimeRecords,TimeMenus
from .models import TimeRecords,TimeMenus
from .models import ProjectName

import datetime
from datetime import timedelta

proj_name = "Project Name"
#proj_name=ProjectName.objects.values_list('project_name', flat=True).get(pk=1)
today = datetime.datetime.now()

def daterange():
    date=datetime.date.today()
    year, week, dow = date.isocalendar()
    if dow == 1:
        start_date = date
    else:
        start_date = date - timedelta(dow)
    end_date = start_date + datetime.timedelta(days=7)
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def timeSheetMenu(request):
    time_menus=TimeMenus.objects.all()
    context={'proj_name':proj_name,'time_menus':time_menus}
    return render(request,'timesheets/index.html', context)

def timeEntryList(request):
    time_records=TimeRecords.objects.filter(ts_date__year=today.year, ts_date__month=today.month)
    context = {'time_records': time_records}
    return render(request, 'timesheets/detail.html', context)

def timeEntryCreate(request):
    date_gen=daterange()
    date_list = list(date_gen)
    date_today=datetime.date.today()
    CreateTimeSheetFormSet = formset_factory(CreateTimeSheetForm, extra=0, max_num=20)
    if request.method == 'POST':
        formset = CreateTimeSheetFormSet(request.POST)
        print(formset)
        if formset.is_valid():
            for form in formset:
                create_form = form.save(commit=False)
                create_form.emp_id = '2014' # because ts_date is excluded
                create_form.save()
            return render(request, 'timesheets/result.html', {'date_list':date_list})
    else:
        formset = CreateTimeSheetFormSet(initial=[{'ts_date': x } for x in date_list])
    return render(request, 'timesheets/create.html', {'formset': formset })

def timeEntryUpdate(request):
    response = "You're updating Time Entry Id ."
    return HttpResponse(response)

def timeEntryDelete(request):
    return HttpResponse("You're deleting  Time Entry Id ." )
