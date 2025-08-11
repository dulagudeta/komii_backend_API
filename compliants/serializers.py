from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Complaint
        fields = '__all__'
        read_only_fields = ['id', 'user', 'status', 'created_at', 'updated_at']
