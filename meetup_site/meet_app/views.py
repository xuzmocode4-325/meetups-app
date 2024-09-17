from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from .models import Meetup
from .forms import RegistrationForm

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
        context['meetup_found'] = self.get_object() is not None
        context['form'] = RegistrationForm()  # Always include a form in the context
        return context

    def post(self, request, *args, **kwargs):
        # Get the current meetup object
        self.object = self.get_object() 
        form = RegistrationForm(request.POST)

        if form.is_valid():
            participant = form.save()
            self.object.attendees.add(participant) # Add the participant to the meetup
            return redirect('success')  # Redirect to a success URL
    
        # If the form is not valid, render the same page with the form errors
        context = self.get_context_data(form=form)  # Reuse the context from get_context_data
        return render(request, self.template_name, context)  
    

class SuccessView(TemplateView):
    template_name = 'meet_app/registration-confirmation.html'
    context_object_name = 'meetup'

