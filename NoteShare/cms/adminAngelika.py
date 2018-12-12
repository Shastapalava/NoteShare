from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *
from .forms import PostAdminForm, CustomUserCreationForm, CustomUserChangeForm

@admin.register(Complaint)
class ComplaintsAdmin(admin.ModelAdmin):
	list_display = ('complainAbout', 'commplainFrom','post','explanation')
	raw_id_fields = ('complainAbout', 'commplainFrom','post')
	

@admin.register(Invitation)
class Invitation(admin.ModelAdmin):
    list_display = ('inviteTo', 'inviteFrom','isApplication','post', 'isAccepted')
    raw_id_fields = ('inviteTo', 'inviteFrom','post')
    #list_editable = ('OUName','on_doc')


# @admin.register(LockPost)
# class LockPost(admin.ModelAdmin)

# def safe_update(request,model,slug):
# 	obj = model.objects.get(slug)
# 	if obj.locked:
# 		print("Locked")
# 	else:
# 	obj.lock()
# 		return update_object(request,model,slug)
