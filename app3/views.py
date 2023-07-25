from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sample(request):
    return HttpResponse('<center><h1> This Is String Responce Page Of App3 </h1></center>')

def index5(request):
    return render(request,'index5.html')

def index6(request):
    return render(request,'index6.html')