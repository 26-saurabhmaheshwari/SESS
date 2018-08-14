from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import CreateTimeSheetForm
from django.forms import formset_factory
from django.contrib import messages
import xlwt
from django.utils import timezone
# Create your views here. from sess_dev.timesheets.models import TimeRecords,TimeMenus
from .models import TimeRecords,TimeMenus
from .models import ProjectName
import datetime
from datetime import timedelta
proj_name = "Project Name"

#proj_name=ProjectName.objects.values_list('project_name', flat=True).get(pk=1)
today = datetime.datetime.now()

def timeSheetMenu(request):
    time_menus=TimeMenus.objects.all()
    context={'proj_name':proj_name,'time_menus':time_menus}
    return render(request,'timesheets/index.html', context)

def timeEntryApprove(request):
    context = dict()
    time_records = TimeRecords.objects.all()
    # emp_id = 2002
    # time_records = TimeRecords.objects.all().filter(emp_id = emp_id)
    current_week = timezone.now().isocalendar()[1]
    current_records = [time_record for time_record in time_records if time_record.get_week() == current_week]
    context['current_records'] = current_records

    if request.method == 'POST':
        emp_id = request.POST['eid']
        time_records = TimeRecords.objects.all().filter(emp_id = emp_id)
        current_week = timezone.now().isocalendar()[1]
        current_records = [time_record for time_record in time_records if time_record.get_week() == current_week]
        context['current_records'] = current_records
        return render(request, 'timesheets/approve_list.html', context)
   

    return render(request, 'timesheets/approve_list.html', context)


def timeEntryList(request):
    context = dict()
    # time_records = TimeRecords.objects.all()
    

    emp_id = 2002
    time_records = TimeRecords.objects.all().filter(emp_id = emp_id)
    current_week = timezone.now().isocalendar()[1]
    current_records = [time_record for time_record in time_records if time_record.get_week() == current_week]
    c_week = current_week
    x_week = current_week
    y_week = current_week

    if request.method == 'POST':
        week = request.POST['week']

        if week == 'selected':
            week_sel = request.POST['week-selected']
            week_no = week_sel[6:8]
            week_no = int(week_no)
            current_records = [time_record for time_record in time_records if
                               time_record.get_week() == week_no ]
            try:
                gotdata = current_records[0]                
                c_week = current_records[0].get_week()
                x_week = current_records[0].get_week()
            except IndexError:
                gotdata = 'null'
                c_week = week_no 
                x_week = ''

        if week == 'next-week':
            week_no = request.POST.get('week_no')
            week_no = int(week_no)
            current_records = [time_record for time_record in time_records if
                               time_record.get_week() == week_no + 1]
            try:
                gotdata = current_records[0]
                
                c_week = current_records[0].get_week()
                x_week = current_records[0].get_week()
            except IndexError:
                gotdata = 'null'
                c_week = week_no 
                x_week = ''
        
        if week == 'last-week':
            week_no = request.POST.get('week_no')
            week_no = int(week_no)
            if not c_week:
                c_week = week_no
            current_records = [time_record for time_record in time_records if
                               time_record.get_week() == week_no - 1]
            try:
                gotdata = current_records[0]
                c_week = current_records[0].get_week()
                y_week = current_records[0].get_week()
            except IndexError:
                gotdata = 'null'
                c_week = week_no 
                y_week = ''

    context['current_records'] = current_records
    context['c_week'] = c_week
    context['x_week'] = x_week
    context['y_week'] = y_week

    return render(request, 'timesheets/list.html', context)

    

def timeEntryCreate(request):

    if request.method == 'POST':
        hours=request.POST['hours']
        task_description=request.POST['task-description']
        try :
            request.POST['task-checked']
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']         
        except:
            date =request.POST['date']
            print ("you didnot check period")
            

    return render(request, 'timesheets/list.html')

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