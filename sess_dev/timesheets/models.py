from django.db import models

# Create your models here.

class TimeRecords(models.Model):
    emp_id = models.IntegerField(verbose_name = 'Employee ID',help_text="Enter The Employee ID")
    ts_date = models.DateField(null=False, blank=False,verbose_name = 'Time Sheet Date',help_text="Enter Time Sheet Date")
    ts_effort = models.IntegerField(verbose_name = 'Hours worked',help_text="Enter The Hours worked")
    ts_desc = models.CharField(max_length=200,verbose_name = 'Time Description',help_text="Enter The task details")

    class Meta:
        verbose_name = 'Time Records'
        verbose_name_plural = 'Time Records'

    def __str__(self):
        return self.ts_desc