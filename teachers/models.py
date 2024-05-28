from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from subjects.models import Subjects


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)
