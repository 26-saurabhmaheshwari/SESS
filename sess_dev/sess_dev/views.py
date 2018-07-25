from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required

class IndexView(View):
    template_name = "home.html"
    def get(self, request):
        return render(request, self.template_name)

@login_required(login_url='/login/')
def Dashboard(request):
    template_name = "index.html"
    return render(request, template_name)
 
    # html = "<html><body>It is now </body></html>" 
    # return HttpResponse(html)