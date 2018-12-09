from django.contrib import admin
<<<<<<< HEAD
from .models import Post, Complain_OU


#from .models import Complain

=======
from reversion_compare.admin import CompareVersionAdmin
from .models import Post
from .forms import PostAdminForm
>>>>>>> bd719373d8dbfc40b09b3b52f4eea85c136d2856

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
<<<<<<< HEAD

admin.site.register(Complain_OU)
class Complain_OUAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	raw_id_fields = ('author',)
=======
	form = PostAdminForm
>>>>>>> bd719373d8dbfc40b09b3b52f4eea85c136d2856
