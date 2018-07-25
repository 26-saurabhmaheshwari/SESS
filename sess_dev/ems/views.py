from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import generic,View
from django.views.generic import TemplateView
from .forms import UserForm
from timesheets.models import TimeRecords


## Class based view 
class EmployeeListView(generic.ListView):
    model = User
    template_name = "ems/employee_list.html"

    def get_queryset(self):
        if self.request.GET.get('q'):
            try:
                first_name = self.request.GET.get('q')
            except :
                first_name = ''
            if (first_name != ''):
                object_list = self.model.objects.filter(first_name__icontains = first_name)
            else:
                object_list = self.model.objects.all()
        else:
            object_list = self.model.objects.all()
        return object_list


class EmployeeDetailView(generic.DetailView):
    model = User
    template_name = "ems/employee_detail.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        
        context['tags'] = TimeRecords.objects.all().filter(emp_id = 2001)
        return context

# For Login
class UserFormView(View):
    form_class = UserForm
    template_name = "ems/registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/employee/')

        return render(request, self.template_name, {'form': form})            

# Create New Employee
def EmployeeCreateView(request):
    form = UserForm(request.POST or None)
    print("Before ")
    print (form.errors)
    if form.is_valid():
        print("after")
        obj = form.save(commit=False)
        obj.save()
        return redirect('/employee/')        

    context = {
         'form' : form
     }
    template = "ems/employee_create.html"
    return render(request, template, context )

# update Employee
def EmployeeUpdateView(request, id):
    obj = get_object_or_404(User, id=id)
    form = UserForm(request.POST or None, instance=obj)
    context = {
        'form' : form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/employee/{num}".format(num=obj.id))

    template = "ems/update-view.html"
    return render(request, template, context )

# Delete the Employee from the table

def EmployeeDeleteView(request, id=None):
    emp = get_object_or_404(User, id=id) 
    if request.method == "POST":
        emp.delete()
        return HttpResponseRedirect("/employee/")
    context = {
        "emp" : emp,
    }
    template = "ems/delete-view.html"
    return render(request, template, context )




