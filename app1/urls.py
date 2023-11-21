from django.urls import *
from app1.views import *
from app2.views import *
app_name='app1'
urlpatterns=[
    path('csk/',csk,name='csk'),
    path('mi/',mi,name='mi'),

]