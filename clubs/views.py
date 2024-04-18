from django.shortcuts import render

# clubs/views.py

from django.shortcuts import render
from .models import Club, Event, Announcement, Discussion, Topic, Comment

def home(request):
    # Retrieve data from your models
    clubs = Club.objects.all()
    events = Event.objects.all()
    announcements = Announcement.objects.all()
    discussions = Discussion.objects.all()
    
    # Pass data to the template
    context = {
        'clubs': clubs,
        'events': events,
        'announcements': announcements,
        'discussions': discussions,
    }
    return render(request, 'clubs/home.html', context)

