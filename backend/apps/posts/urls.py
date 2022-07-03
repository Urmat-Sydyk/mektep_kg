from django.urls import path
from .views import *
from backend.apps.school_info.views import *
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('', SchoolInfoView.as_view(), name='school_info'),
    path('about_us/', AboutUsView.as_view(), name='about'),

]
