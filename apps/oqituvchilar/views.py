from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Teacher
from .forms import TeacherForm
from apps.login.mixins import JWTLoginRequiredMixin

class TeacherListView(JWTLoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'oqituvchilar/teacher_list.html'
    context_object_name = 'teachers'
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self):
        qs = super().get_queryset()

        full_name = self.request.GET.get("full_name")
        bolim = self.request.GET.get("ishlagan_bolimi")
        lavozim = self.request.GET.get("ishlagan_lavozimi")
        pasport = self.request.GET.get("pasport")

        if full_name:
            qs = qs.filter(
                first_name__icontains=full_name
            ) | qs.filter(
                last_name__icontains=full_name
            )

        if bolim:
            qs = qs.filter(ishlagan_bolimi=bolim)

        if lavozim:
            qs = qs.filter(ishlagan_lavozimi=lavozim)

        if pasport:
            qs = qs.filter(pasport__icontains=pasport)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["kafedralar"] = Teacher.choises_kafedra
        context["lavozimlar"] = Teacher.choises_lavozimi
        return context

class TeacherCreateView(
    JWTLoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    model = Teacher
    form_class = TeacherForm
    template_name = 'oqituvchilar/teacher_form.html'
    success_url = reverse_lazy('teachers:teacher_list')
    permission_required = 'oqituvchilar.add_teacher'
    success_message = "O‘qituvchi muvaffaqiyatli qo‘shildi ✅"

    def form_valid(self, form):
        return super().form_valid(form)


class TeacherUpdateView(
    JWTLoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = Teacher
    form_class = TeacherForm
    template_name = 'oqituvchilar/teacher_form.html'
    success_url = reverse_lazy('teachers:teacher_list')
    permission_required = 'oqituvchilar.change_teacher'
    success_message = "O‘qituvchi ma’lumotlari yangilandi ✏️"


class TeacherDeleteView(
    JWTLoginRequiredMixin,
    DeleteView
):
    model = Teacher
    template_name = 'oqituvchilar/teacher_confirm_delete.html'
    success_url = reverse_lazy('teachers:teacher_list')
    permission_required = 'oqituvchilar.delete_teacher'
