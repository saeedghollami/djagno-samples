from django.contrib.auth import views as auth_view
from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", auth_view.LogoutView.as_view(), name="logout",),
]
