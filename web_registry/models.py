from django.db import models
import datetime
from users.models import Patient


class Entry(models.Model):
    date = models.DateTimeField("Date", default=datetime.datetime.now)
    CHOICES = [('N', 'Note'),
               ('R', 'Results')]
    entry_type = models.TextField(max_length=1, choices=CHOICES, blank=True)
    value = models.TextField(max_length=1000, blank=True)
    upload = models.ImageField(upload_to='upload/', blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)

