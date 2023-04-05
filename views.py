from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
def hello(request):
    return HttpResponse("Welcome to Django")

def hi(request):
    return HttpResponse("Hello there,Karimi")

def get(request):
    return HttpResponse("Welcome Karimi")

def create(request):
    return HttpResponse("Made my app")



def evenodd(request):
    x = 20
    if x%2==0:
        return HttpResponse("number is even")
    else:
        return HttpResponse("number is odd")


def error(request):
    x = 20
    if x==30:
       return HttpResponse("Page not found")
    else:
        return HttpResponseNotFound("Page found")

def index(request):
    return render(request, 'index.html')

def tables(request):
    return render(request, 'tables.html')

def emptable(request):
    return render(request, 'emptable.html')

def image(request):
    return render(request, 'image.html')



def variables(request):
    details= {
        "firstname":"Faith",
        "lastname":"eMobilis",
        "age":34
    }
    return render(request, 'variables.html', details)

def employee(request):
    details= {
        "Employeename":"Faith",
        "Employeeid":2,
        "salary":34000
    }
    return render(request, 'emp.html', details)
