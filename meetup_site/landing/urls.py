from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('about/', views.about, name='about'),
    path('brands/', views.brands, name='brands'),
    path('contact/', views.contact, name='contact')
]

