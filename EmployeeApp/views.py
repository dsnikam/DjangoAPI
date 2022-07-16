from operator import index, truediv
import re
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees,dt,RawData
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer,dtSerializer,RawDataSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",save=False)

@csrf_exempt
def rawdataApi(request):
    if request.method == 'GET':
        rawdata = RawData.objects.all()
        rawdata_serializer = RawDataSerializer(rawdata, many=True)
        return JsonResponse(rawdata_serializer.data,safe=False)
    elif request.method=='POST':
        rawdata_data = JSONParser().parse(request)
        rawdata_serializer=RawDataSerializer(data=rawdata_data)
        if rawdata_serializer.is_valid():
            rawdata_serializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        rawdata_data = JSONParser().parse(request)
        rawdata = RawData.objects.get(_id=rawdata_data['_id'])
        rawdata_serializer=RawDataSerializer(rawdata,data=rawdata_data)
        if rawdata_serializer.is_valid():
            rawdata_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        rawdata=RawData.objects.get(_id=id)
        rawdata.delete()
        return JsonResponse("Deleted Successfully",save=False)
    
def index(request):
  mymembers = RawData.objects.all().values()
  output = ""
  for x in mymembers:
    output += '"'
    #output += str(x["ep"])
    output += str(x["dt"]["tm"])
    output += '"'
  return HttpResponse(output)

