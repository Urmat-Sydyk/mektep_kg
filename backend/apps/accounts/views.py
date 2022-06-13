from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import FormView, CreateView, TemplateView

from backend.apps.accounts.forms import LoginForm, UserRegisterForm, ProfileForm


class UserProfilePage(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        pin = data['pin']
        password = data['password']
        user = authenticate(pin=pin, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('user_profile')
            else:
                return HttpResponse('Ваш аккаунт не активен')
        return HttpResponse('Такого пользователя не сушествует или пароль неверный')


def userRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your account has been successfully created')
            return redirect('sign_in')
    else:
        form = UserRegisterForm()
        profile_form = ProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'register.html', context)


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('sign_in')
