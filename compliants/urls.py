from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet, CategoryViewSet
from django.urls import path
from .views import admin_report
router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet, basename='complaint')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls + [
    path('reports/admin/', admin_report, name='admin-report'),
]