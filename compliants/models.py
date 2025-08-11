from django.db import models
from django.conf import settings

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('declined', 'Declined'),
    ]

    TYPE_CHOICES = [
        ('road', 'Road Issue'),
        ('water', 'Water Issue'),
        ('electricity', 'Electricity Issue'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='complaint_photos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.status}"
