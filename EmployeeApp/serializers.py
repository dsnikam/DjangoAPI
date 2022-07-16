from dataclasses import field
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees, dt, RawData

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId','DepartmentName')
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')

class dtSerializer(serializers.ModelSerializer):
    class Meta:
        model = dt
        fields = ('tm','hm','pp','wd','ws','sm','st','sc','lt','lw','bl','pv')
    
class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = ('dd','vn','ep','dt')