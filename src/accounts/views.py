from django.shortcuts import render, redirect  
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from .models import *
from .admin import UserCreationForm
from .utils import AppointmentMixin
from .forms import LogInForm, UserAppointmentForm


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/register.html',
                      context={'form': form})

    def post(self, request):
        bound_form = UserCreationForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('login_url')
        return render(request, 'accounts/register.html',
                      context={'form': bound_form})


class AppointmentView(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        if request.user.is_authenticated:
            form = UserAppointmentForm()
            id_user = request.user.id
            user = MyUser.objects.get(id=id_user)
            return render(request, 'accounts/appointment.html',
                          context={'form': form, 'user': user})
        return redirect('login_url')


    def post(self, request):
        bound_form = UserAppointmentForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('profile_url')
        return render(request, 'accounts/appointment.html', context={'form': bound_form})



def history_view(request):
    print()
    #print(dir(request))
    print()
    print(request.POST)
    print()
    pass


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile_url')
        else:
            form = LogInForm()
            return render(request, 'accounts/login.html', context={'form': form})

    def post(self, request):
        bound_form = LogInForm(request.POST)
        if bound_form.is_valid():
            data = bound_form.cleaned_data
            email = data.get('email')
            password = data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_url')
            return render(request, 'accounts/login.html', context={'form': bound_form})
        return render(request, 'accounts/login.html', context={'form': bound_form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home_url')


def profile_view(request):
    if request.user.is_authenticated:
        id_user = request.user.id
        user_profile = MyUser.objects.get(id=id_user)
        return render(request, 'accounts/profile.html', context={'user_profile': user_profile})
    return redirect('login_url')


class EditView(View):
    def get(self, request):
        id = request.user.id
        user = MyUser.objects.get(id=id)
        bound_form = UserCreationForm(instance=user)
        return render(request, 'accounts/edit.html',
                      context={'form': bound_form, 'user': user})

    def post(self, request):
        id = request.user.id
        user = MyUser.objects.get(id=id)
        bound_form = UserCreationForm(request.POST, instance=user)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('login_url')
        return render(request, 'accounts/edit.html',
                      context={'form': bound_form, 'user': user})