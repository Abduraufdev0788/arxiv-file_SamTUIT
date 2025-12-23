from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View

from apps.login.models import Registration

class IndexView(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="index.html")
    
class HomeView(View):
    def get(self, request:HttpRequest)->HttpResponse:
        user_id = request.session.get('user_id')
        if not user_id:
            return JsonResponse({"message":"login not defound"})
        if not Registration.objects.filter(id = user_id):
            return redirect("registratsiya:register")
        return render(request=request, template_name="home/home.html")
