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

# # Custom User Stuff
# class CustomUserCreationForm(UserCreationForm):

#     is_OU = forms.BooleanField()
#     pend_OU = forms.BooleanField()
#     class Meta:
#         model = User
#         fields = ('username', 'first_name' , 'last_name', 'is_OU', 'pend_OU')
#     def save(self, commit=True):
#         CustomUser = super(UserCreateForm, self).save(commit=False)
#         CustomUser.is_currently_an_OU = self.cleaned_data["is_OU"]
#         CustomUser.pending_OU = self.cleaned_data["pend_OU"]
#         if commit:
#             CustomUser.save()
#         return CustomUser

#     # class Meta(UserCreationForm):
#     #     model = CustomUser
#     #     fields = ('username', 'email', 'is_currently_an_OU')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'is_currently_an_OU')