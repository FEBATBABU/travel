from django.http import HttpResponse
from django.shortcuts import render
from . models import  place,blog


# Create your views here.
def fun(request):
    obj=place.objects.all()
    return render(request,"index.html",{'results': obj})




def func(request):
    obt = blog.objects.all()

    return render(request,"index.html", {'finals': obt})
