from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import RegisterView, GetTokenView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('get-token/', GetTokenView.as_view(), name='get-token'),

    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/logout/', LogoutView.as_view(), name='logout'),
]