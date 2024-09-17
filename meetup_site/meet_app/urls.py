
from django.urls import path
from . import views

urlpatterns = [
    path(
        'meetups/', 
        views.IndexView.as_view(), 
        name='all-meetups'),
     path('meetups/success!',
        views.SuccessView.as_view(),
        name='sucess'),
    path(
        'meetups/<slug:meetup_slug>', 
        views.MeetupDetailView.as_view(),
        name='meetup-details'),
]
