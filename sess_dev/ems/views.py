from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic,View
from django.views.generic import TemplateView
from .forms import UserForm
from timesheets.models import TimeRecords
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin



## Class based view 
class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "ems/employee_list.html"
    login_url = '/login/'

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
            object_list = self.model.objects.all().exclude(is_superuser = 1)
        return object_list


# class EmployeeDetailView(UserPassesTestMixin, generic.DetailView):
class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "ems/employee_detail.html"
    login_url = '/login/'
  
    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['tags'] = TimeRecords.objects.all().filter(emp_id = 2001)
        return context
    # def test_func(self):
    #     return self.request.user.email.endswith('@example.com')

# # For Login
# class UserFormView(View):
#     form_class = UserForm

# Create New Employee
def EmployeeCreateView(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return redirect('/employee/') 

    context = { 'form' : form }
    template = "ems/registration_form.html"
    return render(request, template, context )

# update Employee
def EmployeeUpdateView(request, id):
    obj = get_object_or_404(User, id=id)
    form = UserForm(request.POST or None, instance=obj)
    context = { 'form' : form }

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
    context = { "emp" : emp }
    template = "ems/delete-view.html"
    return render(request, template, context )


@login_required(login_url='/login/')
def Profile(request):
    template = "ems/profile.html"
    emp = get_object_or_404(User, username='rparihar') 
    context = { "emp" : emp }
    return render(request, template, context )



