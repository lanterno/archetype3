from django.urls import path
from djoser import views

from .views import UserProfileView

urlpatterns = [
    path("token/login", views.TokenCreateView.as_view(), name="login"),
    path("token/logout", views.TokenDestroyView.as_view(), name="logout"),
    path("profile", UserProfileView.as_view(), name="profile"),
]
