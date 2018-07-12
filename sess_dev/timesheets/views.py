from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import CreateTimeSheetForm
from django.forms import formset_factory
from django.contrib import messages
import xlwt


# Create your views here.
from .models import TimeRecords,TimeMenus
from .models import ProjectName

import datetime
from datetime import timedelta

proj_name=ProjectName.objects.values_list('project_name', flat=True).get(pk=1)
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
    return render(request, 'timesheets/list.html', context)

def timeEntryCreate(request):
    date_gen=daterange()
    date_list = list(date_gen)
    date_today=datetime.date.today()
    CreateTimeSheetFormSet = formset_factory(CreateTimeSheetForm, extra=0, max_num=20)
    if request.method == 'POST':
        formset = CreateTimeSheetFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                create_form = form.save(commit=False)
                create_form.emp_id = '1214' # because ts_date is excluded
                create_form.save()
            #return render(request, 'timesheets/result.html', {'date_list':date_list})
            messages.success(request, "Time Sheet Created Successfully")
            return HttpResponseRedirect("/timesheets/view")
    else:
        formset = CreateTimeSheetFormSet(initial=[{'ts_date': x } for x in date_list])
    return render(request, 'timesheets/create.html', {'formset': formset })

def timeEntryUpdate(request, id):
    obj = get_object_or_404(TimeRecords, id=id)
    form = CreateTimeSheetForm(request.POST or None, instance=obj)
    context = {
        'form' : form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Time Entry Updated")
        return HttpResponseRedirect("/timesheets/view")
    template = "timesheets/update.html"
    return render(request, template, context )

def timeEntryDelete(request, id):
    obj = get_object_or_404(TimeRecords, id=id) 
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Time Entry Deleted")
        return HttpResponseRedirect("/timesheets/view")
    context = {
        "id" : obj,
    }
    template = "timesheets/delete.html"
    return render(request, template, context )

def timeEntryExport(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="timeEntryExport.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Current')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    date_style = xlwt.easyxf(num_format_str='YYYY/MM/DD')


    columns = ['Date', 'Efforts', 'Description', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows=TimeRecords.objects.values_list('ts_date', 'ts_effort', 'ts_desc')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num], datetime.date):
                ws.write(row_num, col_num, row[col_num], date_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response