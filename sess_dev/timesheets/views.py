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

def days_between_ends(start_date,end_date):
    delta = end_date - start_date         # timedelta
    for i in range(delta.days + 1):
        yield start_date + timedelta(i)

def timeSheetMenu(request):
    time_menus=TimeMenus.objects.all()
    context={'proj_name':proj_name,'time_menus':time_menus}
    return render(request,'timesheets/index.html', context)

def timeEntryList(request):
    context = dict()
    time_records = TimeRecords.objects.all()
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
    date_gen=daterange()
    date_list = list(date_gen)
    date_today=datetime.date.today()
    CreateTimeSheetFormSet = formset_factory(CreateTimeSheetForm, extra=0, max_num=20)
    if request.method == 'POST':
        form_no = request.POST['form_no']

        if form_no == 'one': 
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            start_date=datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
            end_date=datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
            date_gen=days_between_ends(start_date,end_date)
            date_list = list(date_gen)
            formset = CreateTimeSheetFormSet(initial=[{'ts_date': x } for x in date_list])
            return render(request, 'timesheets/create.html', {'formset': formset })

      
        if form_no == 'two':
            formset = CreateTimeSheetFormSet(request.POST)
            if formset.is_valid():
                print("formset is valid ")
                for form in formset:
                    print("printing forms 2")
                    create_form = form.save(commit=False)
                    create_form.emp_id = '2001' # because ts_date is excluded
                    create_form.save()
                #return render(request, 'timesheets/result.html', {'date_list':date_list})
                messages.success(request, "Time Sheet Created Successfully")
                return HttpResponseRedirect("/timesheets/view")
            else:
                print("formset is invalid for form 2")
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

def timeEntryApprove(request, id):
    obj = get_object_or_404(TimeRecords, id=id) 
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Time Entry Approve")
        return HttpResponseRedirect("/timesheets/view")
    context = {
        "id" : obj,
    }
    template = "timesheets/approve.html"
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