from __future__ import unicode_literals
from django.db import models
from ..login.models import User
from datetime import date, time

class AppointmentManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['task']) < 1:
            errors['task'] = "Enter a tasks."
        if len(postData['status'])<1:
            errors['status']="Enter a status"
        if len(postData['date']) < 1:
            errors['date'] = "Enter a Data."
        elif postData['date'] < str(date.now()):
            errors['date'] = "Date must be in the future."
        if len(postData['time']) < 1:
            errors['time'] = "Enter a Time."
        elif postData['time'] < str(time.now()):
            errors['time'] = "time must be in the future."
        return errors



class Appointments(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TextField()
    users = models.ManyToManyField(User, related_name="tasks")
    objects = AppointmentManager()
