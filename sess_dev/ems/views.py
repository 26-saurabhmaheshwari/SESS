from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login

from .forms import EmployeeForm, UserForm
from django.db.models import Q
from .models import Employee, Salaries
from timesheets.models import TimeRecords,TimeMenus
from django.views import generic

from django.views.generic import TemplateView
from django.views import View
import datetime
from datetime import timedelta
today = datetime.datetime.now()  
# from ;lib

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_employee= Employee.objects.all().count()
    #emp_id=Employee.objects.all().filter('emp_id')
    title="Employee Home"
   
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_emp':num_employee, 'title': title},
    )

## Class based view 
class EmployeeListView(generic.ListView):
    model = Employee

    #blank form
 


class EmployeeDetailView(generic.DetailView):
    model = Employee
    
    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        
        context['tags'] = TimeRecords.objects.all().filter(emp_id = 2001)
        return context



# Create user 

class UserFormView(View):
    form_class = UserForm
    template_name = "ems/registration_form.html"
    #template_name = '/ems/registration_form.html' # Get req when accessing
    
    #blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #cleaned normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User Objects if credential is correct 
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/employee/')

        return render(request, self.template_name, {'form': form})            


         



    

# Create

# retrieve

# Update

# Delete

# List

# Function Based view


# Create New Employee
def EmployeeCreateView(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Crerated new user")
        return HttpResponseRedirect("/employee/{num}".format(num=obj.emp_no))

        

    context = {
        'form' : form
    }
    template = "ems/employee_create.html"
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


def EmployeeDetailView1(request, emp_no=None):
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

def EmployeeListView1(request):
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

