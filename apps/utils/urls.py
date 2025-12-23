from django.urls import path

from .views import IndexView, HomeView

app_name = "index"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dashboard/", HomeView.as_view(), name="home_page"),
]
