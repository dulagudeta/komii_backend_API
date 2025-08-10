from django.contrib import admin
from .models import Complaint, ComplaintImage

# Register your models here.
admin.site.register(Complaint)
admin.site.register(ComplaintImage)