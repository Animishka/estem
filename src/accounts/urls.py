from django.urls import path

from .views import *


urlpatterns = [
    path('appointment/', AppointmentView.as_view(), name='appointment_url'),
    path('history/', history_view, name='history_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('register/', RegisterView.as_view(), name='register_url'),
    path('profile/', profile_view, name='profile_url'),
    path('edit/', EditView.as_view(), name='edit_url'),
]