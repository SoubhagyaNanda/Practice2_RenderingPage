from django.urls import path
from app3.views import *
app_name= 'somethingSomething'

urlpatterns=[
    path('sample/',sample,name='sample'),
    path('index5/',index5,name='index5'),
    path('index6/',index6,name='index6'),
]