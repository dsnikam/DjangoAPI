from django.conf.urls import url
from django.urls import path
from EmployeeApp import views

from datetime import datetime

urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),

    # From here on I am editing
    
    #url(r'^rawdata$',views.rawdataApi),
    #url(r'^rawdata/([0-9]+)$',views.rawdataApi),

    #path('',views.index,name='index')
    #url(r'^getdata$',views.getApi),
    url('get-version',views.getversionApi), # a.) part and also c.) part
    url('get-dd',views.getdeviceidApi), # b.) part
    #path('get-version-on-date',views.getdatewiseversionApi), # c.) part
    #url('rawdata',views.RawDataViewset.as_view())
    #url(r'^blah/',views.getdatewiseversionApi),
    #url(r'^get-version-on-date/(?P<date>\d{2}-\d{2}-\d{4})',views.inefficientdatewsieversionapi), #c.) part inefficient
    url(r'^get-days-1-less-(?P<n>[0-9]+)-data',views.getnumberofdaysapi), #d.) part
    url(r'^get-highest values ',views.datewisehighesttempapi), # e.) part
    url(r'get-data-points ',views.getnoofdataptsapi), # f.) part

]
