import calendar
from operator import index, truediv
import re
import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView

from EmployeeApp.models import Departments,Employees,RawData
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer,RawDataSerializer, dtSerializer,versionSerializer

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
'''
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
'''
    
# From here on I am editing

def index(request):
  mymembers = RawData.objects.all().values()
  output = ""
  for x in mymembers:
    output += '"'
    #output += str(x["ep"])
    output += str(x["dt"]["tm"])
    output += '"'
  return HttpResponse(output)

@csrf_exempt
def getApi(request):
    rawdata = RawData.objects.all()
    rawdata_serializer = dtSerializer(rawdata, many=True)
    return JsonResponse(rawdata_serializer.data,safe=False)

@csrf_exempt
def getversionApi(request):
    rawdata = RawData.objects.all().values()
    output = []
    for x in rawdata:
        output.append(str(x["vn"]))
    output=list(set(output))
    '''
    out = ""
    for x in output:
        out += '"'
        #output += str(x["ep"])
        out += str(x)
        out += '"'
    return HttpResponse(out)
    '''
    data = {
    'status': 'versions extracted successfully',
    'payload': output
    }
    return JsonResponse(data)

@csrf_exempt
def getdeviceidApi(request):
    rawdata = RawData.objects.all().values()
    output = []
    for x in rawdata:
        output.append(x["dd"])
    output=list(set(output))
    data={
        'status':'Device ids extracted successfully',
        'payload':output
    }
    return JsonResponse(data)

@csrf_exempt
def getdatewiseversionApi(request,*args,**kwargs):
    rawdata = RawData.objects.all().values()
    rawdataserializer = versionSerializer(rawdata,many=True)
    params = kwargs
    print(params)
    '''
    #date = params["date"]
    dateepoch=calendar.timegm(time.strptime(date, '%d-%m-%Y'))
    #rawdata = RawData.objects.get(dateepoch<ep<dateepoch+86400)
    rawdata = RawData.objects.get(ep=dateepoch)
    output=[]
    for x in rawdata:
        output.append(x["vn"])
    data={
    'status': 'versions extracted successfully for required date',
 	'payload': output
    }
    return JsonResponse(data)
    '''
    return JsonResponse(rawdataserializer.data,safe=False)

def datewsieversionapi(request,date):
    dateepoch=calendar.timegm(time.strptime(date, '%d-%m-%Y'))
    #rawdata = RawData.objects.get(dateepoch<ep<dateepoch+86400)
    
    rawdata = RawData.objects.filter(ep>dateepoch,ep<dateepoch+86400)
    output=[]
    for x in rawdata:
        output.append(x["vn"])
    data={
    'status': 'versions extracted successfully for required date',
 	'payload': output
    }
    return JsonResponse(data)

def inefficientdatewsieversionapi(request,date):
    dateepoch=calendar.timegm(time.strptime(date, '%d-%m-%Y'))
    #rawdata = RawData.objects.get(dateepoch<ep<dateepoch+86400)
    rawdata = RawData.objects.all().values()
    #rawdata = RawData.objects.filter(ep>dateepoch,ep<dateepoch+86400)
    output=[]
    for x in rawdata:
        if x["ep"]>=dateepoch and x["ep"]<dateepoch+86400:
            output.append(x["vn"])
    data={
    'status': 'versions extracted successfully for required date',
 	'payload': output
    }
    return JsonResponse(data)

def getnumberofdaysapi(request,n):
    n=n
    daystart=1617235200
    #the count should be done using filter itself

def datewisehighesttempapi(request,date):
    dateepoch=calendar.timegm(time.strptime(date, '%d-%m-%Y'))
    rawdata = RawData.objects.all().values()
    #rawdata = RawData.objects.filter(ep>dateepoch,ep<dateepoch+86400)
    t=0
    h=0
    for x in rawdata:
        if x["ep"]>=dateepoch and x["ep"]<dateepoch+86400:
            if x["dt"]["tm"]>t:
                t=x["dt"]["tm"]
            if x["dt"]["hm"]>h:
                h=x["dt"]["hm"]
    output={'tm':t,'hm':h}    
    data={
    'status': 'versions extracted successfully for required date',
 	'payload': output
    }
    return JsonResponse(data)