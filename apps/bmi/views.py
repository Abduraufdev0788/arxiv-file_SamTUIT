from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from .models import BmiTalaba
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import BmiTalabaForm
from apps.login.mixins import JWTLoginRequiredMixin, AdminOnlyMixin


class TableView(JWTLoginRequiredMixin, AdminOnlyMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
  
        q = request.GET.get("q", "").strip()

        qs = BmiTalaba.objects.all().order_by('-id')

        if q:
            qs = qs.filter(
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q) |
                Q(group_name__icontains=q) |
                Q(theme_name__icontains=q) |
                Q(years__icontains=q) |
                Q(faculty__icontains=q)
            )

        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'talabalar': page_obj,  
            'page_obj': page_obj,   
            'q': q,                 
        }

        return render(request, 'bmi/index.html', context)
    




class BmiTalabaCreateView(JWTLoginRequiredMixin, AdminOnlyMixin, CreateView):
    model = BmiTalaba
    form_class = BmiTalabaForm
    template_name = 'bmi/create.html'
    success_url = reverse_lazy('bitiruv:bmi')


class BmiTalabaUpdateView(JWTLoginRequiredMixin, AdminOnlyMixin, UpdateView):
    model = BmiTalaba
    form_class = BmiTalabaForm
    template_name = 'bmi/edit.html'
    success_url = reverse_lazy('bitiruv:bmi')

class BmiTalabaDeleteView(JWTLoginRequiredMixin, AdminOnlyMixin, DeleteView):
    model = BmiTalaba
    success_url = reverse_lazy('bitiruv:bmi')
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)




