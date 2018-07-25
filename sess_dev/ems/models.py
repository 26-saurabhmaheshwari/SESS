from django.db import models
from django.urls import reverse 

# Create your models here.
'''
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    emp_no = models.IntegerField(primary_key=True)
    emp_id = models.IntegerField(verbose_name = 'Employee ID eg 2001')
    birth_date = models.DateField(verbose_name = 'Employee DOB eg 1990-01-01',)
    first_name = models.CharField(max_length=14, verbose_name = 'Employee First Name',)
    last_name = models.CharField(max_length=16, verbose_name = 'Employee Last Name',)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name = 'Employee Gender',)
    hire_date = models.DateField(verbose_name = 'Employee Hire Date',)

    def __str__(self):
       return self.first_name

    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.emp_no)])

    class Meta:
        db_table = 'employees'
        verbose_name = 'Employee '
        verbose_name_plural = 'Employees'
'''