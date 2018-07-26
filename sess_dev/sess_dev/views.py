from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def Dashboard(request):
    template_name = "index.html"
    return render(request, template_name)