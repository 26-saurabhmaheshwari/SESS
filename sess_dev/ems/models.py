from django.db import models

# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField(verbose_name = 'Employee DOB',)
    first_name = models.CharField(max_length=14, verbose_name = 'Employee First Name',)
    last_name = models.CharField(max_length=16, verbose_name = 'Employee Last Name',)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name = 'Employee Gender',)
    hire_date = models.DateField(verbose_name = 'Employee Hire Date',)

    def __str__(self):
       # return 'first_name=%s, last_name=%s' % (self.first_name, self.last_name)
       return self.first_name

    class Meta:
        db_table = 'employees'
        verbose_name = 'Employee '
        verbose_name_plural = 'Employees'


class Departments(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4, verbose_name = 'Department No')
    dept_name = models.CharField(unique=True, max_length=40, verbose_name = 'Department',)

    def __str__(self):
       return self.dept_name

    class Meta:
        db_table = 'departments'
        verbose_name = 'Department '
        verbose_name_plural = 'Departments'


class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no', on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Departments, models.CASCADE, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
       return self.emp_no

    class Meta:
        db_table = 'dept_emp'
        unique_together = (('emp_no', 'dept_no'),)


class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no', on_delete=models.CASCADE)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
       return self.salary

    class Meta:
        db_table = 'salaries'
        verbose_name = 'salary '
        unique_together = (('emp_no', 'from_date'),)


class Titles(models.Model):
    emp_no = models.ForeignKey(Employee, models.CASCADE, db_column='emp_no')
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'titles'