from django.shortcuts import render
from django.views import View
from apps.bmi.models import BmiTalaba
from apps.professorlar.models import Professor
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView
from apps.oqituvchilar.models import Teacher
from apps.talabalar.models import Talabalar
from apps.qarorlar.models import PQaror
from apps.qarorlar.models_hokim import HQaror
from apps.qarorlar.models_vazir import VQaror
from apps.qarorlar.models_direktor import DQaror
from django.utils import timezone
from datetime import timedelta

class HomeView(View):
    def get(self, request):
        return render(request, "Customs/home/home.html")
    
class TableView(View):
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

        
        qs = qs.values(
            "first_name",
            "last_name",
            "faculty",
            "group_name",
            "theme_name",
            "years",
        )

        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "talabalar": page_obj,
            "page_obj": page_obj,
            "q": q,
        }

        return render(request, "Customs/bmi/index.html", context)


class ProfessorListView(ListView):
    model = Professor
    template_name = 'Customs/professors/index.html'
    context_object_name = 'professors'
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self):
        qs = super().get_queryset().only(
            'first_name',
            'last_name',
            'qabul_sana',
            'chiqish_sana',
            'ishlagan_fakultet',
            'ishlagan_bolimi',
            'is_active',
        )

        full_name = self.request.GET.get("full_name")
        bolim = self.request.GET.get("ishlagan_bolimi")
        fakultet = self.request.GET.get("ishlagan_fakultet")
        pasport = self.request.GET.get("pasport")

        if full_name:
            qs = qs.filter(
                Q(first_name__icontains=full_name) |
                Q(last_name__icontains=full_name)
            )

        if bolim:
            qs = qs.filter(ishlagan_bolimi=bolim)

        if fakultet:
            qs = qs.filter(ishlagan_fakultet=fakultet)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["kafedralar"] = Professor.choises_kafedra
        context["fakultetlar"] = Professor.choises_fakutet
        return context


class TeacherListView(ListView):
    model = Teacher
    template_name = 'Customs/xodimlar/index.html'
    context_object_name = 'teachers'
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self):
        qs = super().get_queryset().only(
            'first_name',
            'last_name',
            'qabul_sana',
            'chiqish_sana',
            'ishlagan_bolimi',
            'ishlagan_lavozimi',
            'is_active',
        )

        full_name = self.request.GET.get("full_name")
        bolim = self.request.GET.get("ishlagan_bolimi")
        lavozim = self.request.GET.get("ishlagan_lavozimi")
        pasport = self.request.GET.get("pasport")

        if full_name:
            qs = qs.filter(
                Q(first_name__icontains=full_name) |
                Q(last_name__icontains=full_name)
            )

        if bolim:
            qs = qs.filter(ishlagan_bolimi=bolim)

        if lavozim:
            qs = qs.filter(ishlagan_lavozimi=lavozim)

        if pasport:
            qs = qs.filter(pasport__icontains=pasport)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["kafedralar"] = Teacher.choises_kafedra
        context["lavozimlar"] = Teacher.choises_lavozimi
        return context
    
class TalabalarView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        talabalar = Talabalar.objects.only(
            "full_name",
            "qabul_yili",
            "faculty",
            "group",
            "status",
        ).order_by("-id")

        full_name = request.GET.get("full_name")
        if full_name:
            talabalar = talabalar.filter(full_name__icontains=full_name)

        faculty = request.GET.get("faculty")
        if faculty:
            talabalar = talabalar.filter(faculty=faculty)

        qabul_yili = request.GET.get("qabul_yili")
        if qabul_yili and qabul_yili.isdigit():
            talabalar = talabalar.filter(qabul_yili=qabul_yili)

        group = request.GET.get("group")
        if group:
            talabalar = talabalar.filter(group=group)

        paginator = Paginator(talabalar, 100)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, "Customs/talabalar/index.html", {
            "talabalar": page_obj,
            "page_obj": page_obj,
            "filters": request.GET
        })

class QarorlarView(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="Customs/qarorlar/index.html")


class PQarorlar(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        

        q = request.GET.get("q")          # qidiruv
        new = request.GET.get("new")      # yangilari

        datas = PQaror.objects.all().order_by('-created_at')

        # 🔍 Qidiruv
        if q:
            datas = datas.filter(
                Q(qaror_num__icontains=q) |
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )

        if new:
            seven_days_ago = timezone.now() - timedelta(days=7)
            datas = datas.filter(created_at__gte=seven_days_ago)

        context = {
            'qarorlar': datas,
            'len': datas.count(),
            'is_new': new
        }

        return render(
            request,
            "Customs/qarorlar/pqarorlar/index.html",
            context
        )
    
class HQarorlar(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        q = request.GET.get("q")         
        new = request.GET.get("new")     

        datas = HQaror.objects.all().order_by('-created_at')

       
        if q:
            datas = datas.filter(
                Q(qaror_num__icontains=q) |
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )

        
        if new:
            seven_days_ago = timezone.now() - timedelta(days=7)
            datas = datas.filter(created_at__gte=seven_days_ago)

        context = {
            'qarorlar': datas,
            'len': datas.count(),
            'is_new': new
        }

        return render(
            request,
            "Customs/qarorlar/hqarorlar/index.html",
            context
        )
    
class VQarorlar(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        q = request.GET.get("q")         
        new = request.GET.get("new")     

        datas = VQaror.objects.all().order_by('-created_at')

       
        if q:
            datas = datas.filter(
                Q(qaror_num__icontains=q) |
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )

        
        if new:
            seven_days_ago = timezone.now() - timedelta(days=7)
            datas = datas.filter(created_at__gte=seven_days_ago)

        context = {
            'qarorlar': datas,
            'len': datas.count(),
            'is_new': new
        }

        return render(
            request,
            "Customs/qarorlar/vqarorlar/index.html",
            context
        )
    
class DQarorlar(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        q = request.GET.get("q")         
        new = request.GET.get("new")     

        datas = DQaror.objects.all().order_by('-created_at')

       
        if q:
            datas = datas.filter(
                Q(qaror_num__icontains=q) |
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )

        
        if new:
            seven_days_ago = timezone.now() - timedelta(days=7)
            datas = datas.filter(created_at__gte=seven_days_ago)

        context = {
            'qarorlar': datas,
            'len': datas.count(),
            'is_new': new
        }

        return render(
            request,
            "Customs/qarorlar/dqaror/index.html",
            context
        )