from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Includes the tasks app URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Add this for obtaining tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Add this for refreshing tokens
]
