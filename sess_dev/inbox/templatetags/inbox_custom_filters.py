from django import template
from django.template.defaultfilters import stringfilter
from ems.models import EmpProfile
from django.contrib.auth.models import User


register = template.Library()


@register.filter(name='get_emp_dtl')
def get_emp_dtl(emp_id, arg):
    username= EmpProfile.objects.all().filter(emp_id=arg).select_related('username')
    
    print(username[0])
    fn = User.objects.all().filter(username=username[0])
    print(fn)

    return fn
