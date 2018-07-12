from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .forms import EmployeeForm
from django.db.models import Q
from .models import Employee, Salaries



from django.views.generic import TemplateView
from django.views import View
    

class AboutView(View):
    x = "This is X view"
    def get(self, request):
         return HttpResponse(self.x)
    
class YAboutView(AboutView):
     x = "Morning to ya"
     
     def get(self, request):
         return HttpResponse(self.x)
    
    

def index(request):
    return HttpResponse("Hello, This is the Home page of the Employee")

# Create

# retrieve

# Update

# Delete

# List

# Create New Employee
def EmployeeCreateView(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Crerated new user")
        return HttpResponseRedirect("/employee/{num}".format(num=obj.emp_no))

    context = {
        'form' : form
    }
    template = "ems/create-view.html"
    return render(request, template, context )


# update Employee
def EmployeeUpdateView(request, emp_no):
    obj = get_object_or_404(Employee, emp_no=emp_no)
    form = EmployeeForm(request.POST or None, instance=obj)
    context = {
        'form' : form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated Employee")
        return HttpResponseRedirect("/employee/{num}".format(num=obj.emp_no))

    template = "ems/update-view.html"
    return render(request, template, context )

# Delete the Employee from the table
def EmployeeDeleteView(request, emp_no=None):
    emp = get_object_or_404(Employee, emp_no=emp_no) 
    if request.method == "POST":
        emp.delete()
        messages.success(request, "Employee Deleted")
        return HttpResponseRedirect("/employee/")
    context = {
        "emp" : emp,
    }
    template = "ems/delete-view.html"
    return render(request, template, context )


def EmployeeDetailView(request, emp_no=None):
    print(emp_no)
    #obj= Employee.objects.get(emp_no=1)
    emp = get_object_or_404(Employee, emp_no=emp_no)
    sal = Salaries.objects.all()
    
    context = {
        "object" : emp,
        "salr" : sal
    }
    template = "ems/detail-view.html"
    return render(request, template, context )

def EmployeeListView(request):
    query = request.GET.get("q", None)
    qs = Employee.objects.all()
    if query is not None:
        qs=qs.filter(
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query)|
            Q(hire_date__icontains=query))

    context = {
        "object_list" : qs,
    }
    template = "ems/list-view.html"
    return render(request, template, context )



@login_required(login_url='/login/')
def LoginRequiredView(request):
    print(request.user)
    qs = Employee.objects.all()
    context = {
        "object_list" : qs,
    }

    if request.user.is_authenticated:
        template = "ems/list-view.html"
    else:
        print("Not Logged In")
        template = "ems/list-view-public.html"
   
   
    return render(request, template, context )

