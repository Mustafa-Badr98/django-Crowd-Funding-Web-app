from django.contrib.auth.forms import  UserCreationForm, SetPasswordForm, PasswordResetForm
from .models import CustomUser
from django import forms
from .models import UserProfile
from django.contrib.auth import get_user_model


class AccountForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number','image' )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'image']


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']