from django.shortcuts import render
from django.views import generic


# Create your views here.
from .models import TimeRecords,TimeMenus
from .models import ProjectName

proj_name=ProjectName.objects.values_list('project_name', flat=True).get(pk=1)

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    time_menus=TimeMenus.objects.all()
    print(time_menus)

    return render(
        request,
        'index.html',
        context={'proj_name':proj_name,'time_menus':time_menus},
    )

def timesheetview(request):
    # Generate counts of some of the main objects
    time_entries=TimeRecords.objects.all()

    return render(
        request,
        'index.html',
        context={'proj_name':proj_name,'time_entries':time_entries},
    )
    
