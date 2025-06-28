from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, InternViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'managers', ManagerViewSet)
router.register(r'interns', InternViewSet)

# Hook router into URLs
urlpatterns = [
    path('', include(router.urls)),
]
