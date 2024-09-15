from django.urls import path
from .views import IndexView, AboutView, BrandsView, ContactView 

urlpatterns = [
    path('', IndexView.as_view(), name=''),
    path('about/', AboutView.as_view(), name='about'),
    path('brands/', BrandsView.as_view(), name='brands'),
    path('contact/', ContactView.as_view(), name='contact')
]

