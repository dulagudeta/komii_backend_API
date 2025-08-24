from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Count

from .models import Complaint
from .serializers import ComplaintSerializer

User = get_user_model()


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all().order_by('-created_at')
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)

    @action(detail=True, methods=['post'], url_path='assign')
    def assign(self, request, pk=None):
        """
        POST /api/complaints/{pk}/assign/
        Body: {"stakeholder_id": <id>, "force": true/false (optional)}
        Only admin/staff users should be allowed to call this.
        """
        complaint = self.get_object()

        # --- Permission check: only admin or staff-like roles can assign ---
        allowed_assigners = {
            getattr(User, 'ROLE_ADMIN', 'admin'),
            getattr(User, 'ROLE_STAFF', 'staff'),
            getattr(User, 'ROLE_STAKEHOLDER', 'stakeholder'),
        }
        # allow Django superuser / is_staff too
        if not (request.user.is_superuser or request.user.is_staff or getattr(request.user, 'role', None) in allowed_assigners):
            return Response({'detail': 'You do not have permission to assign complaints.'}, status=status.HTTP_403_FORBIDDEN)

        stakeholder_id = request.data.get('stakeholder_id')
        if not stakeholder_id:
            return Response({'detail': 'stakeholder_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            stakeholder = User.objects.get(pk=stakeholder_id)
        except User.DoesNotExist:
            return Response({'detail': 'Stakeholder not found.'}, status=status.HTTP_404_NOT_FOUND)

        # --- Validate assignee is a stakeholder-like user ---
        allowed_assignees = {
            getattr(User, 'ROLE_STAFF', 'staff'),
            getattr(User, 'ROLE_STAKEHOLDER', 'stakeholder'),
            getattr(User, 'ROLE_ADMIN', 'admin'),
        }
        if getattr(stakeholder, 'role', None) not in allowed_assignees and not stakeholder.is_staff:
            return Response({'detail': 'User is not a valid stakeholder.'}, status=status.HTTP_400_BAD_REQUEST)

        # Optional: require stakeholders to be approved if you use is_approved flag
        if hasattr(stakeholder, 'is_approved') and not stakeholder.is_approved:
            return Response({'detail': 'Stakeholder is not approved yet.'}, status=status.HTTP_400_BAD_REQUEST)

        # Optional: if complaint already assigned, require "force" to overwrite
        force = bool(request.data.get('force', False))
        if complaint.assigned_to and not force:
            return Response({
                'detail': 'Complaint already assigned.',
                'assigned_to': complaint.assigned_to.id
            }, status=status.HTTP_400_BAD_REQUEST)

        # Assign and update status
        complaint.assigned_to = stakeholder
        # Only change status to in_progress if it's new (you can adjust logic)
        if complaint.status == Complaint.STATUS_NEW:
            complaint.status = Complaint.STATUS_IN_PROGRESS
        complaint.save()

        serializer = self.get_serializer(complaint, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_report(request):
    # Count complaints by status
    status_counts = Complaint.objects.values('status').annotate(total=Count('status'))

    # Count complaints by category
    category_counts = Complaint.objects.values('category').annotate(total=Count('category'))

    # Complaints per stakeholder
    stakeholder_counts = Complaint.objects.values('assigned_to__username').annotate(total=Count('assigned_to'))

    data = {
        "status_counts": status_counts,
        "category_counts": category_counts,
        "stakeholder_counts": stakeholder_counts
    }
    return Response(data)