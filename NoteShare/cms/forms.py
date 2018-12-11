# used in general
from django import forms

# used to create custom form for posts
from .models import Post

# used for the CustomUser Class
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Post Stuff
class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','author', 'body',)

# Custom User Stuff
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')