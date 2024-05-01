from django import forms
from django.contrib.auth.models import User
from .models import MemberProfile
from .models import LeaderProfile
from .models import Club, Event, Announcement, Discussion, Topic, Comment

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['picture', 'first_name', 'last_name', 'gender','course','bio']
class LeaderProfileForm(forms.ModelForm):
    class Meta:
        model = LeaderProfile
        fields = ['picture', 'first_name', 'last_name', 'gender','club','course','bio']
class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['club', 'title']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['discussion', 'title']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['topic', 'content', 'user']        