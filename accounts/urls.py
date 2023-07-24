from django.urls import path
from accounts.views import account_login_view, account_logout_view, sign_up_view


urlpatterns = [
    path("login/", account_login_view, name="login"),
    path("logout/", account_logout_view, name="logout"),
    path("signup/", sign_up_view, name="signup"),
]
