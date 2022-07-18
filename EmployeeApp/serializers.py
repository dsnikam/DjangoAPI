from dataclasses import field, fields
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees, RawData

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId','DepartmentName')
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')
    
class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = ('dd','vn','ep','dt')
        
#From here on I am editing:-

class dtSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = ['dt']

class versionSerializer(serializers.ModelSerializer):
    class Meta:
        model=RawData
        fields=['vn','ep']