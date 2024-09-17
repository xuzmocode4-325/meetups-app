from django import forms
from .models import Attendee

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email']
        labels = {
           "name": "Your Name", 
            "email": "Your Email",
        }
