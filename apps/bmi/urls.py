from django.urls import path
from .views import TableView

app_name = "bmi"

urlpatterns = [
    path("bmi/", TableView.as_view(), name = "bmi")
]
