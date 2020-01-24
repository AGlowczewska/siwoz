from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOICES = [('D', 'Doctor'),
               ('P', 'Patient')]
    account_type = models.TextField(max_length=1, choices=CHOICES, blank=True)

    def is_doctor(self):
        if self.account_type == 'D':
            return True
        else:
            return False


class Doctor(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=30, blank=True)


class Patient(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True)