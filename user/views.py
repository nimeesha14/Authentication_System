import random
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from user.models import User,UserProfile
from user.form import RegisterForm,UserProfileForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpRequest, HttpResponse

def generate_otp() -> str:
    """Generate a 6-digit OTP as a string."""
    return str(random.randint(100000, 999999))

class RegisterView(View):
    """Handle user registration and send OTP via email."""
    template_name = 'user/register.html'
    form_class = RegisterForm

    def get(self, request:HttpRequest) -> HttpResponse:
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request:HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            otp = generate_otp()
            user.otp = otp
            user.is_verified = False
            user.save()

            # Send OTP email
            send_mail(
                'Email Verification OTP',
                f'Your OTP is {otp}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            request.session['email'] = user.email
            messages.success(request, "OTP sent to your email.")
            return redirect('verify_otp')
        else:
            messages.error(request, "User already exists.")
        return render(request, self.template_name, {'form': form})


class VerifyOTPView(View):
    """Verify OTP and mark user as verified."""
    template_name = "user/otpverify.html"

    def get(self, request:HttpRequest) -> HttpResponse:
        return render(request, self.template_name)

    def post(self, request:HttpRequest) -> HttpResponse:
        email = request.session.get('email')
        otp = request.POST.get('otp')
        user = User.objects.get(email=email)
        if user.otp == otp:
            user.is_verified = True
            # user.otp = None
            user.save()
            messages.success(request, "Email verified successfully.")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP.")
            return redirect('verify_otp')


class LoginView(View):
    """Handle authenticate user login."""

    template_name = 'user/login.html'

    def get(self, request:HttpRequest) -> HttpResponse:
        return render(request, self.template_name)

    def post(self, request:HttpRequest) -> HttpResponse:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_verified:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect('index')
            else:
                messages.error(request, "User is not verified.")
                return redirect('login')
        else:
            messages.error(request, "Invalid email or password.")
        return redirect('login')

class LogoutView(View):
    """Log out the current user."""
    def get(self,request:HttpRequest) -> HttpResponse:
        request.session.flush()
        messages.success(request, "Logout successfully.")
        return redirect('login')



class Userview(View):
    """Display user profile and form."""
    template_name = 'user/index.html'
    form_class = UserProfileForm

    def get(self, request: HttpRequest) -> HttpResponse:
        """Render profile page and show projects if user is authenticated."""
        form = self.form_class()

        if request.user.is_authenticated:
            profile = UserProfile.objects.filter(user=request.user)
        else:
            profile = []

        return render(request, self.template_name, {'form': form, 'profile': profile})

