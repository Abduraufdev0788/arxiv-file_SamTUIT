from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

class TableView(View):
    def get(self, reaquest:HttpRequest)->HttpResponse:
        return render(request=reaquest, template_name="bmi/index.html")