from django.contrib import admin
from .models import MemberProfile
from .models import LeaderProfile

# Register your models here.
admin.site.register(MemberProfile)
admin.site.register(LeaderProfile)