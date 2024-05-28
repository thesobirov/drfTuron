from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from classes.models import Classes


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, blank=True, null=True)
