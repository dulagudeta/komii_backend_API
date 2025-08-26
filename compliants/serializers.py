from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = "__all__"
        read_only_fields = ['reported_by', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if 'status' in validated_data:
            if not request.user.is_staff:  
                raise serializers.ValidationError("You are not allowed to change the status.")
        return super().update(instance, validated_data)
