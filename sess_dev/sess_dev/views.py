from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from ems.models import EmpProfile



class IndexView(View):
    template_name = "home.html"
    def get(self, request):
        return render(request, self.template_name)


@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    request.session['isLoggedIn'] = True
    request.session['isAdmin'] = user.is_superuser
    request.session['email'] = user.email
    request.session['username'] = user.username
    username  = request.session.get('username')
    request.session['emp_id'] = EmpProfile.objects.filter(username_id__exact = request.user.id).values('emp_id')[0]['emp_id']
    
    isLoggedIn = request.session.get('isLoggedIn',False)
    isAdmin = request.session.get('isAdmin',False)
    email = request.session.get('email','')
    emp_id = request.session.get('emp_id')
    request.session.save()

    return render(
        request,
        'registration/login.html',
        context = {'isLoggedIn':isLoggedIn,'isAdmin':isAdmin,'email':email, 'emp_id':emp_id},
    )

@login_required(login_url='/login/')
def Dashboard(request):
    template = "index.html"

    emp_id = request.session.get('emp_id')
    username = request.session.get('username')
    emp = get_object_or_404(User, username=username) 
    context = { "emp" : emp }
    return render(request, template, context )


def error(request):
    template = "error.html"

    
    return render(request, template )


