from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View

from apps.login.models import Registration
from .models import PQaror

class QarorlarView(View):
    def get(self, request):
        user_id = request.session.get('user_id')
        if not user_id:
            return JsonResponse({"message":"login not defound"})
        if not Registration.objects.filter(id = user_id):
            return redirect("registratsiya:register")
        return render(request=request, template_name="qarorlar/qarorlar.html")
    
class PQarorlar(View):
    def get(self, request:HttpRequest)->HttpResponse:
        user_id = request.session.get('user_id')
        
        if not user_id:
            return JsonResponse({"message": "Login topilmadi"}, status=401)
        if not Registration.objects.filter(id=user_id).exists():
            return redirect("registratsiya:register")
        

        datas = PQaror.objects.all().order_by('-created_at')
        

        context = {
            'qarorlar': datas,  
            'len': datas.count()  
        }
        
        print(f"Jami qarorlar soni: {datas.count()}")
        
        return render(
            request=request,
            template_name="qarorlar/prezident_qarorlari/index.html",
            context=context
        )
class QarorQoshish(View):
    def get(self, request:HttpRequest)->HttpResponse:
        user_id = request.session.get('user_id')
        if not user_id:
            return JsonResponse({"message":"login not defound"})
        if not Registration.objects.filter(id = user_id):
            return redirect("registratsiya:register")
        return render(request=request, template_name="qarorlar/prezident_qarorlari/qaror_qoshish.html")
    
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

class QarorView(View):
    def put(self, request:HttpRequest, pk)->HttpResponse:
        user_id = request.session.get("user_id")

        if not user_id:
            return JsonResponse({"message":"login not defound"})
        
        if not Registration.objects.filter(id = user_id):
            return redirect("registratsiya:register")
        
        qaror_put = PQaror.objects.get(id = pk)
        if not qaror_put:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_num = request.PUT.get("qaror_num")
        title = request.PUT.get("title")
        created_at = request.PUT.get("created_at")
        description = request.PUT.get("description")
        file = request.FILES.get("file")
        if qaror_num:
            qaror_put.qaror_num = qaror_num
        if title:
            qaror_put.title = title
        if created_at:
            qaror_put.created_at = created_at
        if description:
            qaror_put.description = description
        if file:
            qaror_put.file = file
        qaror_put.save()
        return redirect("qarorlar:qaror_edit")



    def post(self,request:HttpRequest, pk)-> HttpResponse:
        user_id = request.session.get("user_id")

        if not user_id:
            return JsonResponse({"message":"login not defound"})
        
        if not Registration.objects.filter(id = user_id):
            return redirect("registratsiya:register")
        
        qaror_delete = PQaror.objects.get(id = pk)
        if not qaror_delete:
            return JsonResponse({"error":"bunday qaror mavjud emas"})
        
        qaror_delete.delete()
        return redirect("qarorlar:prezident_qarorlari")



    