from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import FormView, CreateView, TemplateView, UpdateView

from backend.apps.accounts.forms import *





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


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('user_profile')
    queryset = User.objects.all()
    model = User

    def test_func(self):    # проверка на совпадение айдишек залогиненного пользователя и айдишки с 'url'
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False


class UserProfilePage(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url=reverse_lazy('logout')
