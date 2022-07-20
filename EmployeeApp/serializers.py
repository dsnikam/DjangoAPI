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

class demoversionSerializer(serializers.ModelSerializer):
    
    _id = serializers.CharField(max_length=150)
    dd = serializers.CharField(max_length=150)
    vn = serializers.CharField(max_length=150)
    #ep = models.CharField(max_length=150)
    ep = serializers.IntegerField()
    dt = serializers.JSONField(default=dict)
    class Meta:
        model = RawData
        fields = ['_id','dd','vn','ep','dt']

    def create(self, validated_data):
        return RawData.objects.create(**validated_data)

    def update(self, rawdata , validated_data):
        newdata = RawData(**validated_data)
        newdata.dd = rawdata.dd
        print(3)
        newdata.save()
        print(4)
        return newdata
        
        
