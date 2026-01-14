from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpRequest, HttpResponse
from .models import BmiTalaba

class TableView(View):
    def get(self, request:HttpRequest)->HttpResponse:
        qs = BmiTalaba.objects.all().order_by('-id')
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'talabalar': page_obj,   
            'page_obj': page_obj,    
        }

        return render(request, 'bmi/index.html', context)