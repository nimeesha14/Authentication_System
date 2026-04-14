from django import forms
from .models import User,UserProfile,Document
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




class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["file"]

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)

        uploaded_file = self.cleaned_data["file"]
        instance.name = uploaded_file.name
        instance.size = round(uploaded_file.size / 1024)  # size in KB

        ext = uploaded_file.name.split(".")[-1].lower()

        if ext == "pdf":
            instance.file_type = "pdf"
        elif ext in ["doc", "docx"]:
            instance.file_type = "doc"
        elif ext in ["jpg", "jpeg", "png", "gif", "webp", "svg"]:
            instance.file_type = "img"
        else:
            instance.file_type = "pdf"   # default, change if you want

        if user and user.is_authenticated:
            instance.added_by = user
            instance.updated_by = user

        if commit:
            instance.save()

        return instance


