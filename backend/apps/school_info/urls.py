from django.urls import path
from .views import *
from ..posts.views import *

urlpatterns = [
    path('', PostListView.as_view(), name='index'),

]
