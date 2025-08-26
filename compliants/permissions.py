from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or getattr(request.user, 'role', None) in ['staff', 'admin']:
            return True
        return obj.user == request.user
def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False