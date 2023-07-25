from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
    return HttpResponse('<h1> This Is String Page Of App1')

def index1(request):
    return render(request,'index1.html')

def index2(request):
    return render(request,'index2.html')