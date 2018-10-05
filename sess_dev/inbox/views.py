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
    
   
# 
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

    def post(self, request, *args, **kwargs):        
            # d = dict(request.POST.items())    
            # 
            emp_id = request.session.get('emp_id')
            try :
                to=request.POST['inbox_to']
                to_list = to.split(",")
                print (to_list)
                from_id = request.session.get('emp_id')
                #sent_date= 2018-09-12
                for to_element in to_list:
                    try:
                        print (to_element)
                        emp_id1 = EmpProfile.objects.all()select_related('to_element').get(emp_id)
                        print (emp_id1)
                    except IntegrityError:
                        pass
                        
               # return timeEntryList(request) 
                
               
                # date_list=list(days_between_ends(start_date, end_date))
                # for date_element in date_list:
                #     try:
                #         tms_create = TimeRecords(emp_id=emp_id,ts_date=date_element,ts_effort=hours,ts_desc=task_description,ts_status='P')
                #         tms_create.save()
                #     except IntegrityError:
                #         dup_msg="The Time Sheet for "+ str(date_element) + " is already present"
                #         messages.warning(request, dup_msg)
                # messages.success(request, "Submitted")
                return timeEntryList(request)
            except Exception:            
                date = request.POST['date']
                print ("you didnot check period")
                try:
                    tms_create = TimeRecords(emp_id=emp_id,ts_date=date,ts_effort=hours,ts_desc=task_description,ts_status='P')
                    tms_create.save() 
                    messages.success(request, "Submitted Successfully")
                    return timeEntryList(request)
                except IntegrityError:
                    dup_msg="The Time Sheet for "+ date + " is already present"
                    messages.warning(request, dup_msg)
                    return timeEntryList(request)

class InboxDetail(LoginRequiredMixin, generic.DetailView):
    model = InboxBody
    template_name = "inbox/inbox_detail.html"
    login_url = '/login/'
  
    
    # def get_context_data(self, **kwargs):
    #     context = super(InboxDetail, self).get_context_data(**kwargs)
    #     emp_id = self.request.session.get('emp_id')
  
    #     context['inbox_headers'] = InboxHeader.objects.all().filter(from_id = emp_id)
    #     return context
