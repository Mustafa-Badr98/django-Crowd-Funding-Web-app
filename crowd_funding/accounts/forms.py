from django.contrib.auth.forms import  UserCreationForm
from .models import CustomUser
from django import forms
from .models import UserProfile


class AccountForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number','image' )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'image']
 