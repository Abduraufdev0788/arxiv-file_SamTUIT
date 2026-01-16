from django import forms
from .models import BmiTalaba


class BmiTalabaForm(forms.ModelForm):
    class Meta:
        model = BmiTalaba
        fields = [
            'first_name',
            'last_name',
            'faculty',
            'group_name',
            'theme_name',
            'years',
            'total_ball',
            'files',
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
            'faculty': forms.Select(attrs={
                'class': 'form-select'
            }),
            'group_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: 210-21'
            }),
            'theme_name': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Bitiruv ishi mavzusi'
            }),
            'years': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2024–2025'
            }),
            'total_ball': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Masalan: 86.5'
            }),
            'files': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
