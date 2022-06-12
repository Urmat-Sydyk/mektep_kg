from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

from backend.apps.accounts.models import User, StudentProfile
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    pin = forms.CharField(
        validators=[validators.MaxLengthValidator(14), validators.MinLengthValidator(14)],
        label='пин',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ПИН'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'autocomplete': 'off',
            'placeholder': 'Пароль'
        })
    )


class UserRegisterForm(UserCreationForm):
    pin = forms.CharField(
        validators=[validators.MaxLengthValidator(14), validators.MinLengthValidator(14)],
        label='ПИН',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ПИН'})
    )
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'}))
    first_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})
    )
    middle_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'})
    )
    phone = forms.CharField(
        validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(10)],
        label='Телефон',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'})
    )
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Дата рождения'})
    )
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль повторно'})
    )
    class Meta:
        model = User
        fields = [
            'pin',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'phone',
            'birthday',
            'address',
        ]


class ProfileForm(forms.ModelForm):
    parent_phone = forms.CharField(
        validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(10)],
        label='Телефон родителя',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Телефон родителя'})
    )

    class Meta:
        model = StudentProfile
        fields = [
            'parent_phone'
        ]
