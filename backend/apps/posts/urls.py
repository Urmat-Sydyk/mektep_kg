from django.urls import path
from .views import *
from backend.apps.school_info.views import *
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('', SchoolInfoView.as_view(), name='school_info'),
    path('about_us/', AboutUsView.as_view(), name='about'),
    path('courses/', CoursesView.as_view(), name='course'),
    path('news/', NewsView.as_view(), name='news'),
    path('contact/', SendMessageView.as_view(), name='contact')

]
