from django.urls import path

from .views import IndexView, HomeView, ContactView

app_name = "index"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dashboard/", HomeView.as_view(), name="home_page"),
    path("contacts/", ContactView.as_view(), name="contacts"),
]
