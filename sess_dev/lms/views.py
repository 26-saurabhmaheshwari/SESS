from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from .models import lms_details
from django.contrib.auth.models import User
from ems.models import EmpProfile
from .forms import lmsCreateForm,lmsViewForm,lmsUpdateForm,lmsApproveForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.views import generic



class lmsList(LoginRequiredMixin, ListView):
    model = lms_details
    login_url = '/login/'
    template_name = "lms/lms_list.html"
    context_object_name = 'lms'  
    
    def get_queryset(self):
        emp_id = self.request.session.get('emp_id')
        queryset = self.model.objects.filter(emp_id = emp_id) 
        return queryset

class lmsCreate(LoginRequiredMixin, CreateView):
    model = lms_details
    login_url = '/login/'
    form_class = lmsCreateForm
    success_url = reverse_lazy('lmsList')
    template_name = "lms/lms_create.html"

class lmsUpdate(LoginRequiredMixin, UpdateView):
    model = lms_details
    login_url = '/login/' 
    form_class = lmsUpdateForm
    template_name = "lms/lms_update.html"
    success_url = reverse_lazy('lmsList')

class lmsDelete(LoginRequiredMixin, DeleteView):
    model = lms_details
    login_url = '/login/' 
    template_name = "lms/lms_delete.html"
    success_url = reverse_lazy('lmsList')


class lmsApprove(LoginRequiredMixin, ListView):
    model = lms_details
    login_url = '/login/' 
    form_class = lmsApproveForm
    template_name = "lms/lms_approve.html"
    context_object_name = 'lms'
    queryset = lms_details.objects.filter(ls_status = 'P')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['EmpUser_list'] = EmpProfile.objects.all()
        return context

    def post(self, request, *args, **kwargs):        
            d = dict(request.POST.items())            
            try:
                ky = list(d.keys())[0]
                d.pop(ky)
                for key, value in d.items():  
                    print ("Id is : " + key)
                    print ("status is :" + value)
                    self.model.objects.filter(id=key).update(ls_status=value)
                
                return  HttpResponseRedirect("/lms/approve/")

            except ValueError:
                print ("Value Eror")
