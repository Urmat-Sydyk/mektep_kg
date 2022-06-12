from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', userRegister, name='register'),
    path('register_done/', RegisterDoneView.as_view(), name='register_done'),

]
