from PIL import Image
from django.shortcuts import render, redirect  
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from django.http import HttpResponse
from .models import *
from .admin import UserCreationForm
from .utils import AppointmentMixin
import PIL
from .forms import LogInForm, UserAppointmentForm, UserPhotoForm



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


class AppointmentView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = UserAppointmentForm()
            user = MyUser.objects.get(id=request.user.id)
            return render(request, 'accounts/appointment.html',
                          context={'form': form, 'user': user})
        return redirect('login_url')

    def post(self, request):
        bound_form = UserAppointmentForm(request.POST)

        if bound_form.is_valid():
            user = MyUser.objects.get(id=request.user.id)
            appointment = user.userappointment_set.create(
                specialist=bound_form.cleaned_data['specialist'],
                date_appointment=bound_form.cleaned_data['date_appointment'],
            )
            return redirect('history_url')
        return render(request, 'accounts/appointment.html', context={'form': bound_form})


def history_view(request):
    if request.user.is_authenticated:
        user = MyUser.objects.get(id=request.user.id)
        appointments = user.userappointment_set.all()
        return render(request, 'accounts/history.html', context={
            'appointments': appointments})
    return redirect('login_url')


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
            else:
                error = 'Such user does not exist'
                return render(request, 'accounts/login.html', context={'form': bound_form, 'not_found': error})
        return render(request, 'accounts/login.html', context={'form': bound_form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home_url')


def delete_confirmation_view(request):
    if request.user.is_authenticated:
        user = MyUser.objects.get(id=request.user.id)
        return render(request, 'accounts/delete.html', context={'user': user})
    return redirect('login_url')


def delete_view(request):
    if request.user.is_authenticated:
        user = MyUser.objects.get(id=request.user.id).delete()
        return redirect('home_url')
    return redirect('login_url')


def profile_view(request):
    if request.user.is_authenticated:
        user_profile = MyUser.objects.get(id=request.user.id)
        userphoto = user_profile.userphoto_set.all()
        return render(request, 'accounts/profile.html', context={
            'user_profile': user_profile,
            'userphoto': userphoto,
        })
    return redirect('login_url')


class EditView(View):
    def get(self, request):
        user = MyUser.objects.get(id=request.user.id)
        bound_form = UserCreationForm(instance=user)
        return render(request, 'accounts/edit.html',
                      context={'form': bound_form, 'user': user})

    def post(self, request):
        id = request.user.id
        user = MyUser.objects.get(id=id)
        bound_form = UserCreationForm(request.POST, instance=user)

        if bound_form.is_valid():
            data = bound_form.cleaned_data
            data.save()
            return redirect('login_url')
        return render(request, 'accounts/edit.html',
                      context={'form': bound_form, 'user': user})
    

@receiver(pre_delete, sender=UserPhoto)
def userphoto_delete(sender, instance, **kwargs):
    instance.photo.delete(False)


class UploadPhotoView(View):

    def get(self, request):
        if request.user.is_authenticated:
            form = UserPhotoForm()
            user = MyUser.objects.get(id=request.user.id)
            return render(request, 'accounts/userphoto.html',
                          context={'form': form, 'user': user})
        return redirect('login_url')

    def post(self, request):
        bound_form = UserPhotoForm(request.POST, request.FILES)
        if bound_form.is_valid():
            user = MyUser.objects.get(id=request.user.id)
            user.userphoto_set.all().delete()
            user.userphoto_set.create(photo=bound_form.cleaned_data['photo'])
            return redirect('profile_url')
        return render(request, 'accounts/userphoto.html', context={'form': bound_form})