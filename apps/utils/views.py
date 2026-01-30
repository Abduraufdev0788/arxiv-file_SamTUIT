from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
import requests

from apps.login.mixins import AdminOnlyMixin


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "Customs/home/home.html")


class HomeView(AdminOnlyMixin, View):
    def get(self, request):
        return render(request, "home/home.html", {
            "user": request.user_jwt
        })


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "home/contacts.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        # 🔒 Validation
        if not name or not email or not message:
            messages.error(request, "Iltimos, barcha maydonlarni to‘ldiring ❌")
            return redirect("index:contacts")

        text = (
            "📩 *Yangi kontakt xabari*\n\n"
            f"👤 Ism: {name}\n"
            f"📧 Email: {email}\n"
            f"💬 Xabar:\n{message}"
        )

        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        }

        try:
            response = requests.post(url, data=payload, timeout=5)

            if response.status_code == 200:
                messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi ✅")
            else:
                messages.error(request, "Telegramga yuborishda xatolik yuz berdi ❌")

        except requests.exceptions.RequestException:
            messages.error(request, "Server bilan bog‘lanib bo‘lmadi ❌")

        return redirect("index:contacts")
