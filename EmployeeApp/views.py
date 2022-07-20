import calendar
from functools import partial
from operator import index, truediv
import time
from bson import ObjectId
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.defaults import bad_request
from requests import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import viewsets,status
from rest_framework.views import APIView
from django.template import loader
from EmployeeApp import serializers


from EmployeeApp.models import Departments,Employees,RawData
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer,RawDataSerializer, dtSerializer,demoversionSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        rawdata_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(rawdata_serializer.data,safe=False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        rawdata_serializer=DepartmentSerializer(data=department_data)
        if rawdata_serializer.is_valid():
            rawdata_serializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        rawdata_serializer=DepartmentSerializer(department,data=department_data)
        if rawdata_serializer.is_valid():
            rawdata_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",save=False)
    
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

'''
@csrf_exempt
def getApi(request):
    rawdata = RawData.objects.all()
    rawdata_serializer = dtSerializer(rawdata, many=True)
    return JsonResponse(rawdata_serializer.data,safe=False)
'''    

@csrf_exempt
def getversionApi(request):
    try:
        params=request.GET
        date=params["date"]
        dateepoch=calendar.timegm(time.strptime(date, '%d-%m-%Y'))
        rawdata = RawData.objects.filter(ep__gte=dateepoch)
        rawdata = rawdata.filter(ep__lt = dateepoch+86400).values()
        output=[]
        for x in rawdata:
            output.append(x["vn"])
        data={
        'status': 'versions extracted successfully for required date',
 	    'payload': output
        }
        return JsonResponse(data)
    except:
        rawdata = RawData.objects.all().values()
        output = []
        for x in rawdata:
            output.append(str(x["vn"]))
        output=list(set(output))
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

'''
@csrf_exempt
def getdatewiseversionApi(request):
    date=request.GET
    date=date["date"]
    dateepoch=calendar.timegm(time.strptime(date, '%d-%m-%Y'))
    rawdata = RawData.objects.filter(ep__gte=dateepoch)
    rawdata = rawdata.filter(ep__lt = dateepoch+86400).values()
    output=[]
    for x in rawdata:
        output.append(x["vn"])
    data={
    'status': 'versions extracted successfully for required date this this',
 	'payload': output
    }
    return JsonResponse(data)
'''

'''
def inefficientdatewsieversionapi(request,date):
    dateepoch=calendar.timegm(time.strptime(date, '%d-%m-%Y'))
    #rawdata = RawData.objects.get(dateepoch<ep<dateepoch+86400)
    rawdata = RawData.objects.all().values()
    output=[]
    for x in rawdata:
        if x["ep"]>=dateepoch and x["ep"]<dateepoch+86400:
            output.append(x["vn"])
    data={
    'status': 'versions extracted successfully for required date',
 	'payload': output
    }
    return JsonResponse(data)
'''

def getnumberofdaysapi(request,n):
    n=int(n)
    daystart=1617235200-86400
    temp=-1
    numofdays=0
    while temp != 0:
        rawdata = RawData.objects.filter(ep__gte = daystart)
        rawdata = rawdata.filter(ep__lt = daystart+86400).values()
        output=[]
        for x in rawdata:
            output.append(x["vn"])
        output = list(set(output))
        temp = len(output)
        if temp == n-1:
            numofdays+=1
        daystart+=86400
    data = {
        'status': 'required number of days extracted',
        'payload': numofdays
    }
    return JsonResponse(data)

def datewisehighesttempapi(request):
    params = request.GET
    date = params["date"]
    dateepoch=calendar.timegm(time.strptime(date, '%d-%m-%Y'))
    #rawdata = RawData.objects.all().values()
    rawdata = RawData.objects.filter(ep__gte = dateepoch)
    rawdata = rawdata.filter(ep__lt = dateepoch+86400).values()
    t=0
    h=0
    for x in rawdata:
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

def getnoofdataptsapi(request):
    params = request.GET
    print(params)
    start_date = params["start_date"]
    end_date = params["end_date"]
    vn = params["vn"]
    vn = vn[1:-1]  # there is a issue of quotation marks solved here
    start_epoch = calendar.timegm(time.strptime(start_date, '%d-%m-%Y'))
    end_epoch = calendar.timegm(time.strptime(end_date, '%d-%m-%Y'))+86400
    rawdata = RawData.objects.filter(ep__gte = start_epoch)
    rawdata = rawdata.filter(ep__lt = end_epoch)
    rawdata = rawdata.filter(vn = vn)
    noofdatapts = rawdata.count()
    payload = {'datapoints':noofdatapts}
    data = {
        'status': 'number of data points for given version extracted',
 	    'payload': payload
    }
    return JsonResponse(data)

'''
@csrf_exempt
def changeversionapi(request,self):
    if request.method=='POST':
        try:
            return super(changeversionapi,self).create(request)
        except IntegrityError:
            return bad_request(request)
        request_data = JSONParser().parse(request)
        rawdata = RawData.objects.filter(ep = request_data['dataepoch'])
        rawdata = rawdata.filter(dd = request_data['dd'])
        if (request_data['new_vn'] in ["92.1.1.1","92.1.1.2","92.1.1.3"]) and len(rawdata)!=0:
            for x in rawdata:
                rawdata_serializer=RawDataSerializer(x,data=request_data,partial=True)
                if rawdata_serializer.is_valid():
                    rawdata_serializer.save()
                else:
                    return Response(data=rawdata_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            data = {'status':'Datapoint successfully updated with new version'}
            return JsonResponse(data,safe=False)
            #return JsonResponse("Failed to Update")
            #for x in rawdata:
            #    x["vn"] = request_data['new_vn']
            #    x.save()
            #data = {'status':'Datapoint successfully updated with new version'}
            #return JsonResponse(data)
        else:
            data={'status':'Bad request'}
            return JsonResponse(data)
'''

@csrf_exempt
def demochangeversionapi(request):
    try:
        if request.method == 'POST':
            request_data = JSONParser().parse(request)
            rawdata = RawData.objects.filter(ep = request_data['dataepoch'])
            rawdata = rawdata.filter(dd = request_data['dd'])
            for x in rawdata:
                print(1)
                x.vn = request_data['new_vn']
                print(2)
                x.save()
                print(3)
            return HttpResponse("Voila")
    except:
        return HttpResponse("something went wrong")
    

    '''
    try:
        request_data = JSONParser().parse(request)
        rawdata = RawData.objects.filter(ep = request_data['dataepoch'])
        rawdata = rawdata.filter(dd = request_data['dd'])
    except:
        return HttpResponse(status=404)

    try:
        if request.method == 'POST':
            #request_data = JSONParser().parse(request)
            #rawdata = RawData.objects.filter(ep = request_data['dataepoch'])
            #rawdata = rawdata.filter(dd = request_data['dd'])
            rdata = rawdata.values()
            print(1)
            print(rdata[0]["_id"])
            print(2)
            req_data = {
                "_id": str(rdata[0]["_id"]),
                "dd" : rdata[0]["dd"],
                "vn" : request_data['new_vn'],
                "ep" : rdata[0]["ep"],
                "dt" : rdata[0]["dt"]
            }
            for x in rawdata:
                rawdata_serializer = demoversionSerializer(x, data = req_data)
                print(2.5)
                if rawdata_serializer.is_valid():
                    print(2.6)
                    rawdata_serializer.save()
                    print(2.7)
                    #return JsonResponse({"message":"Update can be performed"}, safe=False)
                    return JsonResponse(rawdata_serializer.data, safe=False)
                else:
                    return JsonResponse(rawdata_serializer.errors, safe=False)
    except:
        print("exception caused")
        return HttpResponse("something's wrong")
    '''
    
    '''
    try:
        request_data = JSONParser().parse(request)
        rawdata = RawData.objects.filter(ep = request_data['dataepoch'])
        rawdata = rawdata.filter(dd = request_data['dd'])
        print(1)
        if (request_data['new_vn'] in ["92.1.1.1","92.1.1.2","92.1.1.3"]) and len(rawdata)!=0:
            for x in rawdata:
                rawdata_serializer=demoversionSerializer(x,data=request_data,partial=True)
                print(2)
                if rawdata_serializer.is_valid():
                    print(3)
                    rawdata_serializer.save()
                    print(4)
                else:
                    return Response(data=rawdata_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            data = {'status':'Datapoint successfully updated with new version'}
            return JsonResponse(data,safe=False)
        else:
            data={'status':'Bad request'}
            return JsonResponse(data)
    except:
        print("Error came")
'''

@csrf_exempt
def deleteapi(request):
    if request.method == 'DELETE':
        request_data = JSONParser().parse(request)
        rawdata = RawData.objects.filter(ep = request_data['dataepoch'])
        rawdata = rawdata.filter(dd = request_data['dd'])
        rawdata.delete()
        return JsonResponse({'status':'Datapoint deleted succesfully'},safe=False)

