from rest_framework import viewsets, permissions

from users import models
from .models import Complaint, Category
from .serializers import ComplaintSerializer, CategorySerializer


class IsOwnerOrAssignedOrAdmin(permissions.BasePermission):
    """
    Custom permission: 
    - Users can view their own complaints
    - Stakeholders can view assigned complaints
    - Admins can view all
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.reported_by == request.user or obj.assigned_to == request.user


class ComplaintViewSet(viewsets.ModelViewSet):
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAssignedOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Complaint.objects.all().order_by('-created_at')
        return Complaint.objects.filter(
            models.Q(reported_by=user) | models.Q(assigned_to=user)
        ).order_by('-created_at')

    def perform_create(self, serializer):
        # reported_by is automatically set in serializer
        serializer.save()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
