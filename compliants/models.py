from django.db import models
from django.conf import settings

# Create your models here.
class Complaint(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_RESOLVED = 'resolved'
    STATUS_DECLINED = 'declined'

    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_RESOLVED, 'Resolved'),
        (STATUS_DECLINED, 'Declined'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='complaints', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_complaints', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ComplaintImage(models.Model):
    complaint = models.ForeignKey(Complaint, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='complaint_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.title} - {self.get_status_display()}"