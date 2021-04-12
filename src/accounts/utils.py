from django.views.generic import View
from django.shortcuts import render

from django.http import HttpResponse
from .models import *


"""
формирование миксинов, то есть если будут схожие фнукции с небольшими
отличающимися сегментами кода, их переносим в переменные
"""

class AppointmentMixin:
    model = None
    template = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        user_appointments = obj.userprofile_email.all()
        return render(request, self.template,
                      context={'user_appointments': user_appointments, self.model.__name__.lower(): obj})

""" а в модуле views наследую этот класс из модуля
class AppointmentView(AppointmentMixin, View):
    model = UserProfile
    template = 'accounts/appointment.html'

"""