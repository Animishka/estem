from django import forms
from django.core.exceptions import ValidationError
from .models import *

"""
def current_user_func(request):
    id_user = request.user.id

    return id_user
"""

class UserAppointmentForm(forms.Form):
    """
    CHOICE_SPECIALIST = (
        ('СI', 'Сosmetologist Ivanov'),
        ('DA', 'Dermatologist Andreev'),
        ('DV', 'Dermatologist Vasilyev'),
        ('CA', 'Сosmetologist Antonov'),
    )

    #specialist = forms.ChoiceField(choices=CHOICE_SPECIALIST)
    #date_appointment = forms.DateTimeInput(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))


    
    specialist = forms.ChoiceField(choices=CHOICE_SPECIALIST)
    date_appointment = forms.DateTimeInput()

    specialist = forms.CharField()
    date_appointment = forms.DateTimeField()

    class Meta:
        model = UserAppointment
        fields = ('specialist', 'date_appointment')
    
    def save(self, **kwargs):
        #id_user = request.user.id
        #specialist = self.cleaned_data.get('specialist')
        #date_appointment = self.cleaned_data.get('date_appointment')
        return self
"""
    specialist = forms.CharField(max_length=20)
    date_appointment = forms.DateTimeField()
    
    #current_user_func(request)
#работает save, но нужно понять как привязку к id делать
    def save(self):
        id_user = current_user_func()
        current_user = MyUser.objects.get(id=id_user)
        new_appointment = current_user.my_user_appointment.create(
            specialist=self.cleaned_data['specialist'],
            date_appointment=self.cleaned_data['date_appointment']
        )
        return new_appointment



class LogInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        #if email and password:
        #    user = MyUser.objects.filter(email=email)
        #    if not user:
        #        raise ValidationError('Such user does not exists')

        return super(LogInForm, self).clean(*args, **kwargs)

        #return self.clean(*args, **kwargs)






