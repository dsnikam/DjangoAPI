from email.policy import default
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

class dt(models.Model):
    tm = models.IntegerField()
    hm = models.IntegerField()
    pp = models.IntegerField()
    wd = models.IntegerField()
    ws = models.IntegerField()
    sm = models.IntegerField()
    sm = models.IntegerField()
    st = models.IntegerField()
    sc = models.IntegerField()
    lt = models.IntegerField()
    lw = models.IntegerField()
    bl = models.IntegerField()
    pv = models.IntegerField()

class RawData(models.Model):
    #_id = models.AutoField(primary_key=True)
    dd = models.CharField(max_length=150)
    vn = models.CharField(max_length=150)
    ep = models.CharField(max_length=150)
    #dt = dt()
    dt = JSONField(default=dict)
    


    