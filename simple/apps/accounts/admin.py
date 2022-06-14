from django.contrib import admin
from simple.apps.accounts.models import User, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
