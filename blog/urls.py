from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', Home.as_view(), name = 'index'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
]