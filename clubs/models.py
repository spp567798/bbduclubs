from django.db import models
from django.contrib.auth.models import User

class MemberProfile(models.Model):
    gender_choices = [
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Dont want to disclose")
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture= models.ImageField(upload_to='profile/')
    gender = models.CharField(max_length=10, choices=gender_choices)
    course = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

class LeaderProfile(models.Model):
    gender_choices = [
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Dont want to disclose")
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture= models.ImageField(upload_to='profile/')
    gender = models.CharField(max_length=10, choices=gender_choices)
    club= models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

class Club(models.Model):
    name = models.CharField(max_length=100)
    club_admin = models.ForeignKey(User, on_delete= models.CASCADE)
    club_logo = models.ImageField(upload_to="club/logos", default="default_club_logo.png")
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Announcement(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Discussion(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Topic(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField(default="👍")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
