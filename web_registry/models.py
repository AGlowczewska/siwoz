from django.db import models
import datetime
from users.models import Patient
from django.contrib.auth.models import User


class Entry(models.Model):
    date = models.DateTimeField("Date", default=datetime.datetime.now)
    CHOICES = [('N', 'Note'),
               ('R', 'Results')]
    entry_type = models.TextField(max_length=1, choices=CHOICES, blank=True)
    value = models.TextField(max_length=1000, blank=True)
    upload = models.ImageField(upload_to='upload/', blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    is_acknowledged = models.BooleanField(default=False)

    def __str__(self):
        return "%s : %s" % (self.date.strftime("%d.%m.%Y %H:%M"), self.value)


class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField("Date", default=datetime.datetime.now)
    autor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    value = models.TextField(max_length=1000, blank=True)