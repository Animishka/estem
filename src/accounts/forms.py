from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, ImageField, widgets

from .models import *


class UserAppointmentForm(forms.Form):
    specialist = forms.ChoiceField(choices=UserAppointment.CHOICE_SPECIALIST)
    date_appointment = forms.DateTimeField()

    specialist.widget.attrs.update({'class': 'form-control'})
    date_appointment.widget.attrs.update({'class': 'form-control'})

    def clean(self, *args, **kwargs):
        try:
            specialist = self.cleaned_data.get('specialist')
            date_appointment = self.cleaned_data.get('date_appointment')
            return super(UserAppointmentForm, self).clean(*args, **kwargs)
        except:
            raise ValidationError('You made a mistake in the entered data')


class LogInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        try:
            email = self.cleaned_data.get('email').strip()
            password = self.cleaned_data.get('password').strip()
            return super(LogInForm, self).clean(*args, **kwargs)
        except:
            raise ValidationError('You made a mistake in the entered data')


class UserPhotoForm(ModelForm):

    class Meta:
        model = UserPhoto
        fields = ['photo']
