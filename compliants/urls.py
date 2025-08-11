from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet, basename='complaint')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls
