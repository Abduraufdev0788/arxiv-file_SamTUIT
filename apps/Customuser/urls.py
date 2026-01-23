from django.urls import path
from .views import HomeView, TableView, ProfessorListView, TeacherListView, TalabalarView, QarorlarView, PQarorlar, HQarorlar, VQarorlar, DQarorlar

app_name = "user"


urlpatterns = [
    path("user/", HomeView.as_view(), name="user_home"),
    path("bmi/", TableView.as_view(), name="bmi"),
    path("professors/", ProfessorListView.as_view(), name="professors"),
    path("xodimlar/", TeacherListView.as_view(), name="xodimlar" ),
    path("talabalar/", TalabalarView.as_view(), name="talabalar"),
    path("qarorlar/", QarorlarView.as_view(), name="qarorlar"),
    path("prezident/", PQarorlar.as_view(), name="prezident"),
    path("hokim/", HQarorlar.as_view(), name="hokim" ),
    path("vazir/", VQarorlar.as_view(), name="vazir" ),
    path("direkor/", DQarorlar.as_view(), name="direktor" ),

]