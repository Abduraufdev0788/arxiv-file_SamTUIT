from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.utils.urls")),
    path('royxatdan_otish/', include("apps.login.urls")),
    path("qarorlar/", include("apps.qarorlar.urls")),
    path("talabalar/", include("apps.talabalar.urls")),
    path("bmi/", include("apps.bmi.urls")),
    path("xodimlar/", include("apps.oqituvchilar.urls")),
    path("professorlar/", include("apps.professorlar.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
