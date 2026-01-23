from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from apps.login.mixins import AdminOnlyMixin


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "index.html")


class HomeView(AdminOnlyMixin, View):
    def get(self, request):
        return render(request, "home/home.html", {
            "user": request.user_jwt
        })
    
class ContactView(AdminOnlyMixin, View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="home/contacts.html")
    
    def post(self, request:HttpRequest)->HttpResponse:
        pass

