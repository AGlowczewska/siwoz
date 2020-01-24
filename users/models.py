from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOICES = [('D', 'Doctor'),
               ('P', 'Patient')]
    account_type = models.TextField(max_length=1, choices=CHOICES, blank=True)
    specialization = models.CharField(max_length=30, blank=True)

    def is_patient(self):
        if self.account_type == 'P':
            return True
        else:
            return False

    def is_doctor(self):
        if self.account_type == 'D':
            return True
        else:
            return False


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
