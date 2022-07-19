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

# Fromm here on I am editing

class RawData(models.Model):
    _id = models.AutoField(primary_key=True)
    dd = models.CharField(max_length=150)
    vn = models.CharField(max_length=150)
    #ep = models.CharField(max_length=150)
    ep = models.BigIntegerField()
    dt = JSONField(default=dict)
    
    def __str__(self):
        return str(self.ep)
    