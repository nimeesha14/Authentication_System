from urllib import request
from django.views import View
from user.models import User,UserProfile
from user.form import RegisterForm,UserProfileForm
from django.shortcuts import render


def index(request):
    return render(request, 'register.html')


class Userview(View):
    template_name = 'index.html'
    form_class = UserProfileForm

    def get(self):
        form = self.UserProfileForm()
        profile = UserProfile.objects.all()
        return render(request, self.template_name, {'form':form, 'profile':profile})



# Create your views here.
