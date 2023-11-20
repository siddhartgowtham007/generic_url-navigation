from django.shortcuts import render

# Create your views here.

def python(request):
    return render(request,'one.html')

def mern(request):
    return render(request,'two.html')


