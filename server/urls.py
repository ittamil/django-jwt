from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import GoogleLoginView,CheckingView

urlpatterns = [
    path('api/checking', CheckingView.as_view(), name='social_auth_callback'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/google', GoogleLoginView.as_view(), name='google_social_auth'),
    path('admin/', admin.site.urls),
]
