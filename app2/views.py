from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sample(request):
    return HttpResponse('<center><h1> This Is String Page Of App2 </h1></center>')

def index3(request):
    return render(request,'index3.html')

def index4(request):
    return render(request,'index4.html')