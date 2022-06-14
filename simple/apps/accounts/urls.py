from django.urls import path
from simple.apps.accounts.views import UserRegistrationView, UserLoginView, UserProfileView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # token API
    path("api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    # view API
    path("api/signup/", UserRegistrationView.as_view()),
    path("api/signin/", UserLoginView.as_view()),
    path("api/profile/", UserProfileView.as_view()),
]
