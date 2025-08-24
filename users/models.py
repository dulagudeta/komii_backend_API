from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    RESIDENT = 'resident'
    STAFF = 'staff'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (RESIDENT, 'Resident'),
        (STAFF, 'Staff'),
        (ADMIN, 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=RESIDENT)

    def is_resident(self):
        return self.role == self.RESIDENT

    def is_staff_member(self):
        return self.role == self.STAFF

    def is_admin(self):
        return self.role == self.ADMIN
    def __str__(self):
        return self.username