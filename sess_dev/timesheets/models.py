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
        ordering = ["-emp_id"]

    def __str__(self):
        return self.ts_desc

class TimeMenus(models.Model):
    menu_id = models.IntegerField(verbose_name = 'Menu ID',help_text="Enter The Menu ID")
    menu_name = models.CharField(max_length=200,verbose_name = 'Menu Name',help_text="Menu Name")
    menu_desc = models.CharField(max_length=200,verbose_name = ' Menu Description',help_text="Menu details")

    class Meta:
        verbose_name = 'Time Menus'
        verbose_name_plural = 'Time Menus'
        ordering = ["menu_name"]

    def __str__(self):
        return self.menu_name

class ProjectName(models.Model):
    project_id = models.IntegerField(verbose_name = 'Project ID',help_text="Enter Project ID")
    project_name = models.CharField(max_length=200,verbose_name = 'Project Name',help_text="Project Name")

    class Meta:
        verbose_name = 'Project Names'
        verbose_name_plural = 'Project Names'
        ordering = ["project_id"]

    def __str__(self):
        return self.project_name