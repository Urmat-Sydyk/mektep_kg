from django import forms

from backend.apps.posts.models import Post
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


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'group',
            'author'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'group': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'group',
            'author'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
