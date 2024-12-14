from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Office Staff'),
        ('librarian', 'Librarian'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
