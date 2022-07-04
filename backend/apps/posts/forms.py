from django import forms

from backend.apps.school_info.models import Message


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'sender_name',
            'email',
            'phone',
            'title',
            'text',
        ]
        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Обращения'}),
        }
