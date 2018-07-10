from django.http import HttpResponse

from django.shortcuts import render
from .models import Employee

def index(request):
    return HttpResponse("Hello, This is the Home page of the Employee")

# Create

# retrieve

# Update

# Delete

# List
def EmployeeListView(request):
    print(request.user)
    qs = Employee.objects.all()
    if request.user.is_authenticated:
        print("Logged In")
    else:
        print("Not Logged In")
    qs = Employee.objects.all()
    
    # return HttpResponse("Employess will be listed here")
    # below render (request, "path to template", "context dictionary {}")
    template = "ems/list-view.html"
    context = {
        "object_list" : qs,
        # "some_dict" : {"abc":123, "name": "rajdeep" },
        # "array_list" : [1,2,3],
        # "boolen_value" : True,

    }
    return render(request, template, context )

