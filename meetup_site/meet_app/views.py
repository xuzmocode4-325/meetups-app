from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from . models import Meetup

# Create your views here.

class IndexView(TemplateView):
    template_name = 'meet_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_meetups'] = True
        context['meetups'] = Meetup.objects.all()
        return context

class MeetupDetailView(DetailView):
    model = Meetup
    template_name = 'meet_app/meetup-details.html'
    context_object_name = 'meetup'
    slug_field = 'slug'
    slug_url_kwarg = 'meetup_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meetup_found'] = True if self.object else False
        return context
