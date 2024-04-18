from django.contrib import admin

from .models import Club, Event, Announcement, Discussion, Topic, Comment


admin.site.register(Club)
admin.site.register(Event)
admin.site.register(Announcement)
admin.site.register(Discussion)
admin.site.register(Topic)
admin.site.register(Comment)

