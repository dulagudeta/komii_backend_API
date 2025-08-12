from rest_framework import serializers
from .models import Complaint, ComplaintImage

class ComplaintImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintImage
        fields = ['id', 'image', 'uploaded_at']

class ComplaintSerializer(serializers.ModelSerializer):
    images = ComplaintImageSerializer(many=True, read_only=True)

    class Meta:
        model = Complaint
        fields = [
            'id', 'title', 'description', 'location', 'category', 
            'status', 'reported_by', 'assigned_to', 
            'created_at', 'updated_at', 'images'
        ]
        read_only_fields = ['status', 'reported_by', 'created_at', 'updated_at']
