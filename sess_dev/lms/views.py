from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import lms_details
from .forms import lmsCreateForm,lmsViewForm


class lmsCreate(CreateView):
    model = lms_details
    form_class = lmsCreateForm
    success_url = reverse_lazy('lmsList')

class lmsList(ListView):
    model = lms_details
    form_class = lmsViewForm