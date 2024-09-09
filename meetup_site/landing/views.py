from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello Home")

def about(request):
    return HttpResponse("Hello About")

def brands(request):
    return HttpResponse("Hello BrandsS")

def contact(request):
    return HttpResponse("Hello Contact")