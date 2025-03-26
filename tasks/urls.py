from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Registers the /tasks/ endpoint

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes from the router
]