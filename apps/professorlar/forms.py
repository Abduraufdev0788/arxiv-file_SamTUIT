from django import forms
from .models import Professor


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = [
            'first_name',
            'last_name',
            'qabul_sana',
            'chiqish_sana',
            'shartnoma_raqami',
            'shartnoma_bekor_sana',
            'ishlagan_bolimi',
            'ishlagan_fakultet',
            'pasport',
            'buyruq',
            'is_active'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familiya'
            }),
            'qabul_sana': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'chiqish_sana': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'shartnoma_raqami': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shartnoma raqami'
            }),
            'shartnoma_bekor_sana': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bekor qilingan shartnoma sanasi'
            }),
            'ishlagan_bolimi': forms.Select(attrs={
                'class': 'form-select'
            }),
            'ishlagan_fakultet': forms.Select(attrs={
                'class': 'form-select'
            }),
            'pasport': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'AA1234567'
            }),
            'buyruq': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 rounded border'
            }),
        }
