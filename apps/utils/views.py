from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "index.html")


class HomeView(View):
    def get(self, request):
        if not getattr(request, "user_jwt", None):
            return redirect("registratsiya:login")

        return render(request, "home/home.html", {
            "user": request.user_jwt
        })
    
class ContactView(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="home/contacts.html")
    
    def post(self, request:HttpRequest)->HttpResponse:
        pass

