from django.urls import path

from .views import Login, Register, Forget_password, SendCode, UpdatePassword, VerifyEmail

app_name = "registratsiya"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("forget_password/", Forget_password.as_view(), name="forget_password" ),
    path("send_code/", SendCode.as_view(), name="sendcode"),
    path("update_password/", UpdatePassword.as_view(), name="update_password" ),
    path("verify/", VerifyEmail.as_view(), name="veritfy"),

]
