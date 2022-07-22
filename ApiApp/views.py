import calendar
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ApiApp.models import RawData

# Create your views here.

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

@csrf_exempt
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

@csrf_exempt
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
    'status': 'highest tm and hm values for given date extracted',
 	'payload': output
    }
    return JsonResponse(data)

@csrf_exempt
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

@csrf_exempt
def changeversionapi(request):
    try:
        if request.method == 'POST':
            request_data = JSONParser().parse(request)
            rawdata = RawData.objects.filter(ep = request_data['dataepoch'])
            rawdata = rawdata.filter(dd = request_data['dd'])
            for x in rawdata:
                x.vn = request_data['new_vn']
                x.save()
            data={'status': 'Datapoint successfully updated with new version'}
            return JsonResponse(data,safe=False)
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def exchangetmhmapi(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        rawdata = RawData.objects.filter(ep = request_data['dataepoch'], dd = request_data['dd'])
        for x in rawdata:
            temp1 = x.dt["hm"]
            temp2 = x.dt["tm"]
            x.dt["hm"] = temp2
            x.dt["tm"] = temp1
            x.save()
        data={'status': 'tm and hm in data point are successfully exchanged'}
        return JsonResponse(data,safe=False)
    
@csrf_exempt
def deleteapi(request):
    if request.method == 'DELETE':
        request_data = JSONParser().parse(request)
        rawdata = RawData.objects.filter(ep = request_data['dataepoch'])
        rawdata = rawdata.filter(dd = request_data['dd'])
        rawdata.delete()
        data={'status':'Datapoint deleted succesfully'}
        return JsonResponse(data,safe=False)
