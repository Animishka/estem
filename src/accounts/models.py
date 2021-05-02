from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# redefinition user manager
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None, phone_number=None):
        """
 Creates and saves a User with the given email, date of
 birth and password.
"""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None, phone_number=None):
        """
 Creates and saves a superuser with the given email, date of
 birth and password.
"""
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# redefinition user model
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        help_text="email address",
        max_length=255,
        unique=True,
    )
    phone_number = models.DecimalField(verbose_name='telephone number',
                                       help_text="telephone number",
                                       max_digits=11, decimal_places=0,
                                       unique=True, blank=False)
    first_name = models.CharField(verbose_name='first name',
                                  help_text="first name",
                                  max_length=100, blank=False)
    last_name = models.CharField(verbose_name='last name',
                                 help_text="last name",
                                 max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']

    def __str__(self):
        return self.email


    def has_perm(self,  perm,  obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self,  app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserAppointment(models.Model):

    email = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    CHOICE_SPECIALIST = (
        ('Сosmetologist Ivanov', 'Сosmetologist Ivanov'),
        ('Dermatologist Andreev', 'Dermatologist Andreev'),
        ('Dermatologist Vasilyev', 'Dermatologist Vasilyev'),
        ('Сosmetologist Antonov', 'Сosmetologist Antonov'),
    )
    specialist = models.CharField(max_length=40,
                              help_text="choose the specialist",
                              choices=CHOICE_SPECIALIST, blank=False)
    date_appointment = models.DateTimeField(auto_now=False,
                                            help_text="choose the date appointment",
                                            auto_now_add=False, blank=False)

    def __str__(self):
        return self.specialist


class UserPhoto(models.Model):
    email = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    photo = models.ImageField(
        null=True,
        blank=True,
    )
