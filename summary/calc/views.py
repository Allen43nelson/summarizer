from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,'home.html',{'name':'Allen1'})

     

def add(request):
    return render(request,"result.html",{"result":request.POST["topic"]})
       

