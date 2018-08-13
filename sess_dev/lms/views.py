from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from .models import lms_details
from .forms import lmsCreateForm,lmsViewForm,lmsUpdateForm,lmsApproveForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.views import generic


class lmsList(ListView):
    model = lms_details
    template_name = "lms/lms_list.html"
    context_object_name = 'lms'  
   # queryset = lms_details.objects.filter(emp_id = "2001") 
   # if not commented it will return only Leaves of specifi user


class lmsCreate(CreateView):
    model = lms_details
    form_class = lmsCreateForm
    success_url = reverse_lazy('lmsList')
    template_name = "lms/lms_create.html"

class lmsUpdate(UpdateView):
    model = lms_details
    form_class = lmsUpdateForm
    template_name = "lms/lms_update.html"
    success_url = reverse_lazy('lmsList')

class lmsDelete(DeleteView):
    model = lms_details
    template_name = "lms/lms_delete.html"
    success_url = reverse_lazy('lmsList')


class lmsApprove(ListView):
    model = lms_details
    form_class = lmsApproveForm
    template_name = "lms/lms_approve.html"
    context_object_name = 'lms'
    queryset = lms_details.objects.filter(ls_status = 'P')

    def post(self, request, *args, **kwargs):        
            d =dict(request.POST.items())            
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
