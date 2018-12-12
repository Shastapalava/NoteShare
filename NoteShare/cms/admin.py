from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin




from .models import *
from .forms import PostAdminForm, CustomUserCreationForm, CustomUserChangeForm

#admin.site.register(Post) #this displays all class elements of Post to be edited. Equivalent to putting every attribute in list_display

@admin.register(Post) #this line does the same thing as admin.site.register(Post), but lets you also create your own ModelAdmin class to choose what you display in the admin interface
class PostAdmin(CompareVersionAdmin):
	list_display = ('title', 'slug', 'author','publish','status','locked') #this doesn't let you edit such things like the date created
	list_filter = ('status', 'created', 'publish','author')
	search_fields = ('title','body')
	#prepopulated_fields = {'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status','publish')
	form = PostAdminForm

@admin.register(ComplainOU)
class ComplainOUAdmin(admin.ModelAdmin):
	list_display = ('OUName', 'reason')
	#raw_id_fields = ('author',)
	
@admin.register(Invitation)
class Invitation(admin.ModelAdmin):
    list_display = ('OUName', 'on_doc')
    raw_id_fields = ('OUName','on_doc')
    #list_editable = ('OUName','on_doc')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','isOU','is_superuser']
	
@admin.register(TabooList)
class TabooListAdmin(admin.ModelAdmin):
    list_display = ('tWord',)
    # raw_id_fields = ('tWord',)

# @admin.register(LockPost)
# class LockPost(admin.ModelAdmin)

# def safe_update(request,model,slug):
# 	obj = model.objects.get(slug)
# 	if obj.locked:
# 		print("Locked")
# 	else:
# 	obj.lock()
# 		return update_object(request,model,slug)


