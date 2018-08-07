from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from .models import lms_details
from .forms import lmsCreateForm,lmsViewForm,lmsUpdateForm
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