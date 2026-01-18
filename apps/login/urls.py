from django.urls import path
from .views import (
    Register,
    VerifyEmail,
    Login,
    ForgetPassword,
    SendCode,
    UpdatePassword,
    LogoutView
)

app_name = "registratsiya"

urlpatterns = [
    # ================= AUTH =================
    path("register/", Register.as_view(), name="register"),
    path("verify/", VerifyEmail.as_view(), name="verify"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # ================= PASSWORD RESET =================
    path("forget-password/", ForgetPassword.as_view(), name="forget_password"),
    path("send-code/", SendCode.as_view(), name="send_code"),
    path("update-password/", UpdatePassword.as_view(), name="update_password"),

]
