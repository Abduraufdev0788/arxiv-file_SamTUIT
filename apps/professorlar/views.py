from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Professor
from .forms import ProfessorForm
from apps.login.mixins import JWTLoginRequiredMixin, AdminOnlyMixin

class ProfessorListView(JWTLoginRequiredMixin, AdminOnlyMixin, ListView):
    model = Professor
    template_name = 'professors/professor_list.html'
    context_object_name = 'professors'
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self):
        qs = super().get_queryset()

        full_name = self.request.GET.get("full_name")
        bolim = self.request.GET.get("ishlagan_bolimi")
        fakultet = self.request.GET.get("ishlagan_fakutet")
        pasport = self.request.GET.get("pasport")

        if full_name:
            qs = qs.filter(
                first_name__icontains=full_name
            ) | qs.filter(
                last_name__icontains=full_name
            )

        if bolim:
            qs = qs.filter(ishlagan_bolimi=bolim)

        if fakultet:
            qs = qs.filter(ishlagan_fakultet=fakultet)

        if pasport:
            qs = qs.filter(pasport__icontains=pasport)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["kafedralar"] = Professor.choises_kafedra
        context["fakultetlar"] = Professor.choises_fakutet
        return context

class ProfessorCreateView(
    JWTLoginRequiredMixin,
    AdminOnlyMixin,
    SuccessMessageMixin,
    CreateView
):
    model = Professor
    form_class = ProfessorForm
    template_name = 'professors/professor_form.html'
    success_url = reverse_lazy('professors:professor_list')
    permission_required = 'professors.add_professor'
    success_message = "Professors muvaffaqiyatli qo‘shildi ✅"

    def form_valid(self, form):
        return super().form_valid(form)


class ProfessorUpdateView(
    JWTLoginRequiredMixin,
    AdminOnlyMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = Professor
    form_class = ProfessorForm
    template_name = 'professors/professor_form.html'
    success_url = reverse_lazy('professors:professor_list')
    permission_required = 'professors.change_professor'
    success_message = "Professor ma’lumotlari yangilandi ✏️"


class ProfessorDeleteView(
    JWTLoginRequiredMixin,
    AdminOnlyMixin,
    DeleteView
):
    model = Professor
    template_name = 'professors/professors_confirm_delete.html'
    success_url = reverse_lazy('professors:professor_list')
    permission_required = 'professors.delete_professor'
