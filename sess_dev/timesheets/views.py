from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render

# Create your views here.
from .models import TimeRecords,TimeMenus
from .models import ProjectName

proj_name=ProjectName.objects.values_list('project_name', flat=True).get(pk=1)

def timeSheetMenu(request):
    time_menus=TimeMenus.objects.all()
    context={'proj_name':proj_name,'time_menus':time_menus}
    return render(request,'timesheets/index.html', context)

def timeEntryList(request):
    time_records=TimeRecords.objects.all()
    context = {'time_records': time_records}
    return render(request, 'timesheets/detail.html', context)

def timeEntryCreate(request):
    response = "You're Creating Time Entry ."
    return HttpResponse(response)

def timeEntryUpdate(request):
    response = "You're updating Time Entry Id ."
    return HttpResponse(response)

def timeEntryDelete(request):
    return HttpResponse("You're deleting  Time Entry Id ." )



'''
def timeEntryView(request):
    time_record_detail = get_list_or_404(TimeRecords)
    return render(request, 'timesheets/detail.html', {'time_record_detail': time_record_detail})
'''


'''

'''