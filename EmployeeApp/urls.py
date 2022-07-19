from django.conf.urls import url
from django.urls import URLPattern, path
from EmployeeApp import views

from django.urls import register_converter
from datetime import datetime

class DateConverter:
    regex = '\d{2}-\d{2}-\d{4}'

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),

    # From here on I am editing
    
    #url(r'^rawdata$',views.rawdataApi),
    #url(r'^rawdata/([0-9]+)$',views.rawdataApi),

    #path('',views.index,name='index')
    url(r'^getdata$',views.getApi),
    url('get-version',views.getversionApi), # a.) part
    url('get-dd',views.getdeviceidApi), # b.) part
    #path('get-version-on-date',views.getdatewiseversionApi), # c.) part
    #url('rawdata',views.RawDataViewset.as_view())
    url(r'^blah/(?P<date>\d{2}-\d{2}-\d{4})',views.datewsieversionapi),
    url(r'^get-version-on-date/(?P<date>\d{2}-\d{2}-\d{4})',views.inefficientdatewsieversionapi), #c.) part inefficient
    url(r'^get-days-1-less-<int:n>-data',views.getnumberofdaysapi), #d.) part
    url(r'^get-highest values /(?P<date>\d{2}-\d{2}-\d{4})',views.datewisehighesttempapi) # e.) part

]

#urlpatterns=[
#    path('',views.index,name='index')
#]