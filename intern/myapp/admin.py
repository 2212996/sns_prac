from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import UserImage,Talk,Tweet
from django.contrib.auth.models import User

# admin.site.register(User)
admin.site.register(UserImage)
admin.site.register(Talk)
admin.site.register(Tweet)
# Register your models here.
