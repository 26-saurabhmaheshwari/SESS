from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from .models import InboxHeader , InboxBody , InboxRecipient
from django.contrib.auth.models import User
from ems.models import EmpProfile
#from .forms import lmsCreateForm,lmsViewForm,lmsUpdateForm,lmsApproveForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.views import generic
import datetime



class InboxList(LoginRequiredMixin, ListView):
    model = InboxHeader
    login_url = '/login/'
    template_name = "inbox/inbox_list.html"
    context_object_name = 'inbox'  
    
   

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            emp_id = self.request.session.get('emp_id')
            # Add in a QuerySet of all the books
            # context['Inbox_list'] = InboxHeader.objects.all().select_related('username')
            context['Inbox_list'] = InboxRecipient.objects.exclude(status='D').filter(to_id=emp_id).select_related('msg_id')
            # Inboxlist = InboxRecipient.objects.all().filter(to_id=emp_id).select_related('msg_id')
            # print (type(Inboxlist[0]))
            context['User_list'] = User.objects.all()
            context['Employee_list'] = EmpProfile.objects.all()
            return context

class InboxDetail(LoginRequiredMixin, generic.DetailView):
    model = InboxBody
    template_name = "inbox/inbox_detail.html"
    login_url = '/login/'
  
    
    # def get_context_data(self, **kwargs):
    #     context = super(InboxDetail, self).get_context_data(**kwargs)
    #     emp_id = self.request.session.get('emp_id')
  
    #     context['inbox_headers'] = InboxHeader.objects.all().filter(from_id = emp_id)
    #     return context
