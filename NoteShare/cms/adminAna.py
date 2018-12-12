from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *
from .forms import PostAdminForm, CustomUserCreationForm, CustomUserChangeForm

@admin.register(Taboo)
class TabooAdmin(admin.ModelAdmin):
	list_display = ('tabooWord', 'isPending')
	def get_queryset(self,request):
		# first get the default queryset for the class
		qs = super(TabooAdmin,self).get_queryset(request)
		# now, if the user is super user (attribute in ), then return all entries, otherwise return nothing
		if request.user.is_superuser:
			return qs
		return Taboo.objects.none()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','is_currently_an_OU','pending_OU','is_superuser']
    # def get_queryset(self,request):
    #     # first get the default queryset for the class
    #     qs = super(CustomUserAdmin,self).get_queryset(request)
	# 	# now, if the user is super user (attribute in ), then return all entries, otherwise return nothing
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(email=request.user.email)