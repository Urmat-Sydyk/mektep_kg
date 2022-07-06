from django import forms

from backend.apps.lessons.models import Grade
from backend.apps.posts.models import Post
from backend.apps.school_info.models import Message


class CreateGradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = [
            'student',
            'subject',
            'value',
            'grade_date',
            'teacher',

        ]
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Студент'}),
            'subject': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Предмет'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Оценка'}),
            'grade_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата'}),
            'teacher': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Преподаватель'}),
        }
