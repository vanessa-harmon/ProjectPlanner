from django.urls import path
from accounts.views import account_login_view


urlpatterns = [
    path("login/", account_login_view, name="login"),
]
