from django.urls import path, include
from rest_auth.views import LogoutView

from .views import UserCreate, Loginview


urlpatterns = [
    path("", UserCreate.as_view(), name="user_create"),
    path("login/", Loginview.as_view(),name="login_view"),
    path("logout/", LogoutView.as_view(), name="login_view"),

    ]