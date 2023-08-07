from django import forms
from .models import EventModel

class EventForm(forms.Form):
    class Meta:
        model = EventModel