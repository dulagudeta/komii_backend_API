from rest_framework import serializers
from .models import Complaint, ComplaintImage, Category


class ComplaintImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintImage
        fields = ['id', 'image', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']


class ComplaintSerializer(serializers.ModelSerializer):
    images = ComplaintImageSerializer(many=True, read_only=True)
    image_files = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Complaint
        fields = [
            'id', 'title', 'description', 'location', 'category', 'status',
            'reported_by', 'assigned_to', 'created_at', 'updated_at',
            'images', 'image_files'
        ]
        read_only_fields = ['id', 'status', 'reported_by', 'assigned_to', 'created_at', 'updated_at', 'images']

    def create(self, validated_data):
        image_files = validated_data.pop('image_files', [])
        request = self.context.get('request')
        validated_data['reported_by'] = request.user  # Automatically set reporter
        
        complaint = Complaint.objects.create(**validated_data)

        # Handle multiple images
        for img in image_files:
            ComplaintImage.objects.create(complaint=complaint, image=img)
        
        return complaint


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'default_assigned_to']
