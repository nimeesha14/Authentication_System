from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from user.models import User,UserProfile
from user.form import RegisterForm,UserProfileForm
from django.contrib.auth import authenticate, login

class RegisterView(View):
    template_name = 'user/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

        else:
            messages.error(request, "user already logged in.")

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('index')
        else:
            messages.error(request, "Invalid email or password.")
        return redirect('login')



class LogoutView(View):
    def get(self,request):
        request.session.flush()
        messages.success(request, "Logout successfully.")
        return redirect('login')

class Userview(View):
    template_name = 'user/index.html'
    form_class = UserProfileForm

    def get(self,request):
        form = self.form_class()
        profile = UserProfile.objects.filter(user=request.user)

        return render(request, self.template_name, {'form': form,'profile': profile})




# Create your views here.
