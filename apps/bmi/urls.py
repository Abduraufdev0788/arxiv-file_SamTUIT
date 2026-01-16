from django.urls import path
from .views import TableView, BmiTalabaCreateView, BmiTalabaUpdateView, BmiTalabaDeleteView

app_name = "bitiruv"

urlpatterns = [
    path("bmi/", TableView.as_view(), name = "bmi"),
    path('add/', BmiTalabaCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', BmiTalabaUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BmiTalabaDeleteView.as_view(), name='delete'),
]
