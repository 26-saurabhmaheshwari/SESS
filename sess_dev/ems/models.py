from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User


class EmpProfile(models.Model):
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    emp_id = models.IntegerField(primary_key=True, verbose_name = 'Employee ID')
    emp_dob = models.DateField(null=False, blank=False, verbose_name = 'Date of Birth')
    emp_doj = models.DateField(null=False, blank=False, verbose_name = 'Date of Joining')
    emp_dot = models.DateField(null=True, blank=True, verbose_name = 'Date of Termination')
    emp_con_primary = models.CharField(max_length=10, verbose_name = 'Primary contact number')
    emp_con_secondary = models.CharField(max_length=10, verbose_name = 'Secondary contact number')
    emp_designation = models.CharField(max_length=200, verbose_name = 'Employee designation')
    emp_department = models.CharField(max_length=50, verbose_name = 'Employee Department')

    class Meta:
        verbose_name = 'Emp Profile'
        verbose_name_plural = 'Emp Profile'
        ordering = ["-emp_id"]

    def __str__(self):
         return str(self.username)
    
