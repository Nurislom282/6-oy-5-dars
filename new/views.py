from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Models,Cars

def main(request: WSGIRequest):
    cars = Cars.objects.all()
    models = Models.objects.all()
    context ={
        'cars':cars,
        'models':models}

    return render(request,'index.html',context=context)

def carmodels(request: WSGIRequest):
    models = Models.objects.all()
    context = {
        'models':models
    }
    return render(request,'models.html',context=context)

def cars(request:WSGIRequest):
    cars = Cars.objects.all()
    context = {
        'cars':cars
    }
    return render(request,'cars.html',context=context)