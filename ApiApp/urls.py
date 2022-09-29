from django.conf.urls import url
from django.urls import path
from ApiApp import views

from datetime import datetime

urlpatterns=[
    # From here on I am editing
    
    url('get-version',views.getversionApi), # a.) part and also c.) part
    url('get-dd',views.getdeviceidApi), # b.) part
    url(r'^get-days-1-less-(?P<n>[0-9]+)-data',views.getnumberofdaysapi), #d.) part
    url(r'^get-highest values ',views.datewisehighesttempapi), # e.) part
    url(r'get-data-points ',views.getnoofdataptsapi), # f.) part
    url(r'^change-version',views.changeversionapi), # g.) part
    url(r'^exchange-tm-hm',views.exchangetmhmapi), # g.) part
    url(r'^delete-data-point',views.deleteapi), # i.) part    

]
