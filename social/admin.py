from django.contrib import admin

from social.models import Userprofile,userpost

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(userpost)