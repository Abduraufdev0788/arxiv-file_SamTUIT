from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.db.models import Q

from django.utils import timezone
from datetime import timedelta

from apps.login.models import Registration
from .models import PQaror
from apps.login.mixins import JWTLoginRequiredMixin

class QarorlarView(JWTLoginRequiredMixin,View):
    def get(self, request):
        return render(request=request, template_name="qarorlar/qarorlar.html")
    
class PQarorlar(JWTLoginRequiredMixin, View):
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

        # 🆕 YANGILARI (oxirgi 7 kun)
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
            "qarorlar/prezident_qarorlari/index.html",
            context
        )
class QarorQoshish(JWTLoginRequiredMixin, View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="qarorlar/prezident_qarorlari/qaror_qoshish.html")
    
    def post(self, request:HttpRequest)->HttpResponse:        
        qaror_num = request.POST.get("qaror_num")
        title = request.POST.get("title")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        file = request.FILES.get("file")

        if  not qaror_num:
            return JsonResponse({"error": "qaror raqami kiritilishi shart!"})
        
        if PQaror.objects.filter(qaror_num = qaror_num).exists():
            return JsonResponse({"error":"bu qaror avval kiritilgan"})
        
        if not title:
            return JsonResponse({"error":"title kiritilishi shart"})
        
        if not created_at:
            return JsonResponse({"error":"qaror sanasini kiriting"})
        
        if not file:
            return JsonResponse({"error":"faylni yuklash shart"})
        
        if not description:
            return JsonResponse({"error":"descrption kiritish shart!"})
        
        new_qaror = PQaror(
            qaror_num = qaror_num,
            title = title,
            created_at = created_at,
            file = file,
            description = description
        )
        new_qaror.save()
        return redirect("qarorlar:prezident_qarorlari")

class QarorView(JWTLoginRequiredMixin, View):
    def post(self,request:HttpRequest, pk)-> HttpResponse:        
        qaror_delete = PQaror.objects.get(id = pk)
        if not qaror_delete:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_delete.delete()
        return redirect("qarorlar:prezident_qarorlari")
    

    def get(self, request:HttpRequest, pk)->HttpResponse:

        qaror = PQaror.objects.get(id = pk)
        if not qaror:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        context = {
            "qaror": qaror
        }
        return render(
            request=request,
            template_name="qarorlar/prezident_qarorlari/qaror_edit.html",
            context=context
        )
    
class QarorTahrirlash(JWTLoginRequiredMixin, View):
    def get(self, request:HttpRequest, pk)->HttpResponse:

        qaror = PQaror.objects.get(id = pk)
        if not qaror:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        context = {
            "qaror": qaror
        }
        return render(
            request=request,
            template_name="qarorlar/prezident_qarorlari/qaror_edit.html",
            context=context
        )
    

    def post(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror_edit = PQaror.objects.get(id = pk)
        if not qaror_edit:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_num = request.POST.get("qaror_num")
        title = request.POST.get("title")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        file = request.FILES.get("file")
        if qaror_num:
            qaror_edit.qaror_num = qaror_num
        if title:
            qaror_edit.title = title
        if created_at:
            qaror_edit.created_at = created_at
        if description:
            qaror_edit.description = description
        if file:
            qaror_edit.file = file
        qaror_edit.save()
        return redirect("qarorlar:prezident_qarorlari")
    



#vazirlik qarorlari

from .models_vazir import VQaror




class VQarorlar(JWTLoginRequiredMixin, View):
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
            "qarorlar/vazirlik_qarorlari/index.html",
            context
        )


class VQarorQoshish(JWTLoginRequiredMixin, View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="qarorlar/vazirlik_qarorlari/qaror_qoshish.html")
    
    def post(self, request:HttpRequest)->HttpResponse:
        
        qaror_num = request.POST.get("qaror_num")
        title = request.POST.get("title")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        file = request.FILES.get("file")

        if  not qaror_num:
            return JsonResponse({"error": "qaror raqami kiritilishi shart!"})
        
        if VQaror.objects.filter(qaror_num = qaror_num).exists():
            return JsonResponse({"error":"bu qaror avval kiritilgan"})
        
        if not title:
            return JsonResponse({"error":"title kiritilishi shart"})
        
        if not created_at:
            return JsonResponse({"error":"qaror sanasini kiriting"})
        
        if not file:
            return JsonResponse({"error":"faylni yuklash shart"})
        
        if not description:
            return JsonResponse({"error":"descrption kiritish shart!"})
        
        new_qaror = VQaror(
            qaror_num = qaror_num,
            title = title,
            created_at = created_at,
            file = file,
            description = description
        )
        new_qaror.save()
        return redirect("qarorlar:vazirlik_qarorlari")
    


class VQarorView(JWTLoginRequiredMixin, View):
    def post(self,request:HttpRequest, pk)-> HttpResponse:
        
        qaror_delete = VQaror.objects.get(id = pk)
        if not qaror_delete:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_delete.delete()
        return redirect("qarorlar:vazirlik_qarorlari")
    

    def get(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror = VQaror.objects.get(id = pk)
        if not qaror:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        context = {
            "qaror": qaror
        }
        return render(
            request=request,
            template_name="qarorlar/vazirlik_qarorlari/qaror_edit.html",
            context=context
        )
    

class VQarorTahrirlash(JWTLoginRequiredMixin, View):
    def get(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror = VQaror.objects.get(id = pk)
        if not qaror:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        context = {
            "qaror": qaror
        }
        return render(
            request=request,
            template_name="qarorlar/vazirlik_qarorlari/qaror_edit.html",
            context=context
        )
    

    def post(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror_edit = VQaror.objects.get(id = pk)
        if not qaror_edit:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_num = request.POST.get("qaror_num")
        title = request.POST.get("title")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        file = request.FILES.get("file")
        if qaror_num:
            qaror_edit.qaror_num = qaror_num
        if title:
            qaror_edit.title = title
        if created_at:
            qaror_edit.created_at = created_at
        if description:
            qaror_edit.description = description
        if file:
            qaror_edit.file = file
        qaror_edit.save()
        return redirect("qarorlar:vazirlik_qarorlari")
    


#hokim qarorlari uchun

from .models_hokim import HQaror

class HQarorlar(JWTLoginRequiredMixin, View):
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
            "qarorlar/hokim_qarorlari/index.html",
            context
        )


class HQarorQoshish(JWTLoginRequiredMixin, View):
    def get(self, request:HttpRequest)->HttpResponse:

        return render(request=request, template_name="qarorlar/hokim_qarorlari/qaror_add.html")
    
    def post(self, request:HttpRequest)->HttpResponse:
        
        qaror_num = request.POST.get("qaror_num")
        title = request.POST.get("title")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        file = request.FILES.get("file")

        if  not qaror_num:
            return JsonResponse({"error": "qaror raqami kiritilishi shart!"})
        
        if HQaror.objects.filter(qaror_num = qaror_num).exists():
            return JsonResponse({"error":"bu qaror avval kiritilgan"})
        
        if not title:
            return JsonResponse({"error":"title kiritilishi shart"})
        
        if not created_at:
            return JsonResponse({"error":"qaror sanasini kiriting"})
        
        if not file:
            return JsonResponse({"error":"faylni yuklash shart"})
        
        if not description:
            return JsonResponse({"error":"descrption kiritish shart!"})
        
        new_qaror = HQaror(
            qaror_num = qaror_num,
            title = title,
            created_at = created_at,
            file = file,
            description = description
        )
        new_qaror.save()
        return redirect("qarorlar:hokim_qarorlari")
    


class HQarorView(JWTLoginRequiredMixin, View):
    def post(self,request:HttpRequest, pk)-> HttpResponse:
        
        qaror_delete = HQaror.objects.get(id = pk)
        if not qaror_delete:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_delete.delete()
        return redirect("qarorlar:hokim_qarorlari")
    

    def get(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror = HQaror.objects.get(id = pk)
        if not qaror:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        context = {
            "qaror": qaror
        }
        return render(
            request=request,
            template_name="qarorlar/hokim_qarorlari/qaror_edit.html",
            context=context
        )
    

class HQarorTahrirlash(JWTLoginRequiredMixin, View):
    def get(self, request:HttpRequest, pk)->HttpResponse:

        qaror = HQaror.objects.get(id = pk)
        if not qaror:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        context = {
            "qaror": qaror
        }
        return render(
            request=request,
            template_name="qarorlar/hokim_qarorlari/qaror_edit.html",
            context=context
        )
    

    def post(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror_edit = HQaror.objects.get(id = pk)
        if not qaror_edit:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_num = request.POST.get("qaror_num")
        title = request.POST.get("title")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        file = request.FILES.get("file")
        if qaror_num:
            qaror_edit.qaror_num = qaror_num
        if title:
            qaror_edit.title = title
        if created_at:
            qaror_edit.created_at = created_at
        if description:
            qaror_edit.description = description
        if file:
            qaror_edit.file = file
        qaror_edit.save()
        return redirect("qarorlar:hokim_qarorlari")
    






#direktor qarorlari uchun


from .models_direktor import DQaror

class DQarorlar(JWTLoginRequiredMixin, View):
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
            "qarorlar/direktor_qarorlari/index.html",
            context
        )


class DQarorQoshish(JWTLoginRequiredMixin, View):
    def get(self, request:HttpRequest)->HttpResponse:

        return render(request=request, template_name="qarorlar/direktor_qarorlari/qaror_qoshish.html")
    
    def post(self, request:HttpRequest)->HttpResponse:

        user_id = request.session.get('user_id')
        if not user_id:
            return JsonResponse({"message":"login not defound"})
        if not Registration.objects.filter(id = user_id):
            return redirect("registratsiya:register")
        
        qaror_num = request.POST.get("qaror_num")
        title = request.POST.get("title")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        file = request.FILES.get("file")

        if  not qaror_num:
            return JsonResponse({"error": "qaror raqami kiritilishi shart!"})
        
        if DQaror.objects.filter(qaror_num = qaror_num).exists():
            return JsonResponse({"error":"bu qaror avval kiritilgan"})
        
        if not title:
            return JsonResponse({"error":"title kiritilishi shart"})
        
        if not created_at:
            return JsonResponse({"error":"qaror sanasini kiriting"})
        
        if not file:
            return JsonResponse({"error":"faylni yuklash shart"})
        
        if not description:
            return JsonResponse({"error":"descrption kiritish shart!"})
        
        new_qaror = DQaror(
            qaror_num = qaror_num,
            title = title,
            created_at = created_at,
            file = file,
            description = description
        )
        new_qaror.save()
        return redirect("qarorlar:direktor_qarorlari")
    


class DQarorView(JWTLoginRequiredMixin, View):
    def post(self,request:HttpRequest, pk)-> HttpResponse:
        
        qaror_delete = DQaror.objects.get(id = pk)
        if not qaror_delete:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_delete.delete()
        return redirect("qarorlar:direktor_qarorlari")
    

    def get(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror = DQaror.objects.get(id = pk)
        if not qaror:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        context = {
            "qaror": qaror
        }
        return render(
            request=request,
            template_name="qarorlar/direktor_qarorlari/qaror_edit.html",
            context=context
        )
    

class DQarorTahrirlash(JWTLoginRequiredMixin, View):
    def get(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror = DQaror.objects.get(id = pk)
        if not qaror:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        context = {
            "qaror": qaror
        }
        return render(
            request=request,
            template_name="qarorlar/direktor_qarorlari/qaror_edit.html",
            context=context
        )
    

    def post(self, request:HttpRequest, pk)->HttpResponse:
        
        qaror_edit = DQaror.objects.get(id = pk)
        if not qaror_edit:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_num = request.POST.get("qaror_num")
        title = request.POST.get("title")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        file = request.FILES.get("file")
        if qaror_num:
            qaror_edit.qaror_num = qaror_num
        if title:
            qaror_edit.title = title
        if created_at:
            qaror_edit.created_at = created_at
        if description:
            qaror_edit.description = description
        if file:
            qaror_edit.file = file
        qaror_edit.save()
        return redirect("qarorlar:direktor_qarorlari")
    
