from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class IndexView(View):
    template_name = "home.html"
    def get(self, request):
        return render(request, self.template_name)

@login_required(login_url='/login/')
def Dashboard(request):
    template = "index.html"
    emp = get_object_or_404(User, username='rparihar') 
    context = { "emp" : emp }
    return render(request, template, context )
