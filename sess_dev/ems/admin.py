from django.contrib import admin
# Register your models here.
from .models import Employee, Departments, DeptEmp, Salaries, Titles

admin.site.register(Employee)
admin.site.register(Departments)
admin.site.register(DeptEmp)
admin.site.register(Salaries)
admin.site.register(Titles)



