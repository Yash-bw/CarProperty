from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        OWNER = "OWNER", 'owner'
        USER = "USER", 'user'

    Roles = models.CharField(max_length=10, choices=Roles.choices, default=Roles.ADMIN)


      # Add custom fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username



