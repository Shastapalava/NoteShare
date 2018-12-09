from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin
from .models import Post,Complain_OU
from .forms import PostAdminForm

#admin.site.register(Post) #this displays all class elements of Post to be edited. Equivalent to putting every attribute in list_display

@admin.register(Post) #this line does the same thing as admin.site.register(Post), but lets you also create your own ModelAdmin class to choose what you display in the admin interface
class PostAdmin(CompareVersionAdmin):
	list_display = ('title', 'slug', 'author','publish','status') #this doesn't let you edit such things like the date created
	list_filter = ('status', 'created', 'publish','author')
	search_fields = ('title','body')
	#prepopulated_fields = {'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status','publish')
	form = PostAdminForm

@admin.register(Complain_OU)
class Complain_OUAdmin(admin.ModelAdmin):
	list_display = ('OU_name', 'reason')
	#raw_id_fields = ('author',)