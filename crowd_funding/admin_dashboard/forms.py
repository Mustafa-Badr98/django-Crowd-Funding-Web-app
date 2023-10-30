import re
from django import forms
from accounts.models import UserProfile, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm as BaseUserChangeForm


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'image' , 'phone_number')

    def email_valid(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exist.")
        return email

    def phone_valid(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^01[0-9]{9}$', phone_number):
            raise forms.ValidationError(
                "Phone number must start with 01 and consist of 11 digits.")
        return phone_number


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['image' ,'username', 'first_name', 'last_name', 'email',  'phone_number']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'password']
        fields = '__all__'
