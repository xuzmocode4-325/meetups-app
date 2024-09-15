from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView): 
    template_name = 'index.html'

class AboutView(TemplateView): 
    template_name = 'about.html'

class BrandsView(TemplateView): 
    template_name = 'brands.html'   
class ContactView(TemplateView): 
    template_name = 'contact.html'