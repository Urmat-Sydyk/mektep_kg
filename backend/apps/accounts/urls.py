from django.urls import path
from .views import *
urlpatterns = [
    path('', UserProfilePage.as_view(), name='user_profile'),
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', userRegister, name='register'),
    path('logout/', user_logout, name='logout')
]
