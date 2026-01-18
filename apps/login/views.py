from random import randint
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Registration
from apps.login.jwt_utils import generate_tokens


def generate_tokens(user: Registration) -> dict:
    refresh = RefreshToken()
    refresh['user_id'] = user.id
    refresh['email'] = user.email

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }

class Register(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "login/register.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

        name = data.get("name")
        surname = data.get("surname")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if not all([name, surname, email, password, confirm_password]):
            return JsonResponse({"message": "All fields required"}, status=400)

        if Registration.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email already exists"}, status=409)

        if password != confirm_password:
            return JsonResponse({"message": "Passwords do not match"}, status=400)

        # sessionga saqlaymiz (verify uchun)
        request.session['reg_data'] = {
            "name": name,
            "surname": surname,
            "email": email,
            "password": make_password(password),
        }

        code = randint(100000, 999999)
        request.session['verify_code'] = str(code)

        send_mail(
            subject="Verification Code",
            message=f"Your verification code is {code}",
            from_email="turkeynumber063@gmail.com",
            recipient_list=[email],
        )

        # ❗ fetch ishlatyapmiz, redirect emas JSON qaytaramiz
        return JsonResponse({"message": "Verification code sent"}, status=200)


class VerifyEmail(View):
    def get(self, request):
        return render(request, "login/veritfy.html")

    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

        input_code = data.get("code")
        session_code = request.session.get("verify_code")

        if not input_code:
            return JsonResponse({"message": "Code required"}, status=400)

        if input_code != session_code:
            return JsonResponse({"message": "Invalid code"}, status=401)

        reg_data = request.session.get("reg_data")
        if not reg_data:
            return JsonResponse({"message": "Session expired"}, status=401)

        Registration.objects.create(**reg_data)

        # session tozalaymiz
        request.session.flush()

        return JsonResponse({"message": "Account verified"}, status=200)


class Login(View):
    def get(self, request):
        return render(request, "login/login.html")

    def post(self, request):
        data = json.loads(request.body)

        email = data.get("email")
        password = data.get("password")

        user = Registration.objects.filter(email=email).first()
        if not user:
            return JsonResponse({"message": "Email not found"}, status=404)

        if not check_password(password, user.password):
            return JsonResponse({"message": "Incorrect password"}, status=401)

        tokens = generate_tokens(user)

        response = JsonResponse({"message": "Login successful"})

        response.set_cookie(
            "access_token",
            tokens["access"],
            httponly=True,
            samesite="Lax"
        )

        return response



class ForgetPassword(View):
    def get(self, request):
        return render(request, "login/forget_password.html")

    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

        email = data.get("email")

        if not email:
            return JsonResponse({"message": "Email required"}, status=400)

        try:
            user = Registration.objects.get(email=email)
        except Registration.DoesNotExist:
            return JsonResponse({"message": "Email not found"}, status=404)

        code = randint(100000, 999999)
        request.session["reset_code"] = str(code)
        request.session["reset_email"] = email

        send_mail(
            subject="Password reset code",
            message=f"Your reset code is {code}",
            from_email="turkeynumber063@gmail.com",
            recipient_list=[email],
        )

        return JsonResponse({"message": "Reset code sent"}, status=200)


class SendCode(View):
    def get(self, request):
        return render(request, "login/reset_code.html")

    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

        input_code = data.get("code")
        session_code = request.session.get("reset_code")

        if not input_code:
            return JsonResponse({"message": "Code required"}, status=400)

        if not session_code:
            return JsonResponse({"message": "Session expired"}, status=401)

        if input_code != session_code:
            return JsonResponse({"message": "Invalid code"}, status=401)

        return JsonResponse({"message": "Code verified"}, status=200)

class UpdatePassword(View):
    def get(self, request):
        return render(request, "login/new_password.html")

    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if not password or not confirm_password:
            return JsonResponse({"message": "Invalid data"}, status=400)

        if password != confirm_password:
            return JsonResponse({"message": "Passwords do not match"}, status=400)

        email = request.session.get("reset_email")
        if not email:
            return JsonResponse({"message": "Session expired"}, status=401)

        user = get_object_or_404(Registration, email=email)
        user.password = make_password(password)
        user.save()


        request.session.pop("reset_email", None)
        request.session.pop("reset_code", None)

        return JsonResponse({"message": "Password updated"}, status=200)


class LogoutView(View):
    def get(self, request):
        response = redirect("registratsiya:login")

        response.delete_cookie("access_token")

        return response