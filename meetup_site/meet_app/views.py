from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

dummy_meetups = [
    {
        'title': 'Fashion Week', 
        'description': '''Catwalk and runway even in the "Big Apple".''',
        'location':'New York', 
        'slug': 'fashion-week-ny'
    },
    {
        'title': 'Fashion Week', 
        'description': '''Catwalk and runway even in the "City of Love".''', 
        'location':'Paris', 
        'slug': 'fashion-week-paris'
    },
]

def index(request):
    context = {}
    context['show_meetups'] = True
    context['meetups'] = dummy_meetups

    return render(
    request, 
    'meet_app/index.html',
    context
)

def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = dummy_meetups[0]
    return render(
        request, 
        'meet_app/meetup-details.html', 
        {
         "meetup": selected_meetup
        }
)