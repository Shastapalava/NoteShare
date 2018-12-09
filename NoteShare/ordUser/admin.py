'''
from . import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.contrib.auth.models import User


class UserInline(admin.StackedInline):
    model = models.ordUser
    can_delete = False
    verbose_name_plural = 'user'


class UserAdmin(BaseUser):
    inlines = (UserInline)


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
'''