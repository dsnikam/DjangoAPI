from django.conf.urls import url
from django.urls import URLPattern, path
from EmployeeApp import views

urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),

    url(r'^rawdata$',views.rawdataApi),
    url(r'^rawdata/([0-9]+)$',views.rawdataApi)
]

#urlpatterns=[
#    path('',views.index,name='index')
#]