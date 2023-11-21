from django.urls import *
from app2.views import *

app_name='app2'

urlpatterns=[
    path('mi/',mi,name='mi'),
]