from django.contrib import admin

from user.models import User,UserProfile,Document

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Document)

# Register your models here.
