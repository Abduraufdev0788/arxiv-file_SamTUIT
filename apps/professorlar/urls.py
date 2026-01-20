from django.urls import path
from .views import (
    ProfessorListView,
    ProfessorCreateView,
    ProfessorUpdateView,
   ProfessorDeleteView,
)
app_name = "professors"

urlpatterns = [
    path('', ProfessorListView.as_view(), name='professor_list'),
    path('create/', ProfessorCreateView.as_view(), name='professor_create'),
    path('<int:pk>/update/', ProfessorUpdateView.as_view(), name='professor_update'),
    path('<int:pk>/delete/', ProfessorDeleteView.as_view(), name='professor_delete'),
]
