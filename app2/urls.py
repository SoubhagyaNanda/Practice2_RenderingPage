from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('sample/',sample,name='sample'),
    path('index3/',index3,name='index3'),
    path('index4/',index4,name='index4'),
]