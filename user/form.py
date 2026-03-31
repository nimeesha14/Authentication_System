from django import forms
from .models import User,UserProfile
from django.contrib.auth.forms import UserCreationForm

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name', 'email', 'password']




class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','project_name','project_url','project_description']