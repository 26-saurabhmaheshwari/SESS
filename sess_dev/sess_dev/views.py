from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views import generic

from django.views.generic import TemplateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


def index(request):
    #response = HttpResponse(content_type='application/json')
    response = HttpResponse(content_type='text/html')
    response.content='<html><head> <title>Home</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous"><style> body{color:Tomato;}</style></head><body></body></head></html>'
    response.write('<nav class="navbar navbar-expand-lg navbar-light bg-light"><a class="navbar-brand" href="#">Navbar</a> <div class="collapse navbar-collapse" > <div class="navbar-nav"><a class="nav-item nav-link active" href="#">Home <span class="sr-only">(current)</span></a><a class="nav-item nav-link " href="/employee/">Employee <span class="sr-only">(current)</span></a> <a class="nav-item nav-link "href="/timesheets/">Sheets <span class="sr-only">(current)</span></a></div></div></nav>')
    response.write('<div class="container">')
    response.write('<h1>Something </h1>')
    
    response.write("</div>")
    #print(dir(response))
    print(response.status_code)
    print(response.cookies)
    return response

class IndexView(View):
    template_name = "home.html"
    def get(self, request):
        return render(request, self.template_name)
    