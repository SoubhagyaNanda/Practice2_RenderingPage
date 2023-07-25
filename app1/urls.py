from django.urls import path
from app1.views import *
app_name='something'

urlpatterns=[
    path('sample/',sample,name='sample'),
    path('index1/',index1,name='index1'),
    path('index2/',index2,name='index2'),
]