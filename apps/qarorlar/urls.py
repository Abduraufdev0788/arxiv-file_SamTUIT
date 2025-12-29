from django.urls import path
from .views import QarorlarView, PQarorlar, QarorQoshish, QarorView

app_name = "qarorlar"

urlpatterns = [
    path("qarorlar/", QarorlarView.as_view(), name="qarorlar_bosh"),
    path("prezident-qarorlari/", PQarorlar.as_view(), name="prezident_qarorlari"),
    path("add_qaror/", QarorQoshish.as_view(), name="qaror_add"),
    path('tahrirlash/<int:pk>/', QarorView.as_view(), name='qaror_edit'),
    path('ochirish/<int:pk>/', QarorView.as_view(), name='qaror_delete'),
]
