from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from .models import lms_details
from .forms import lmsCreateForm,lmsViewForm,lmsUpdateForm

class lmsList(ListView):
    model = lms_details
    template_name = "lms/lms_list.html"

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