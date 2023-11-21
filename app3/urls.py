from django.urls import *
from app3.views import *

app_name='app3'

urlpatterns=[
    path('rcb/',rcb,name='rcb'),
]