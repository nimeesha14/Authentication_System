from django import forms
from .models import User,UserProfile

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','project_name','project_url','project_description']