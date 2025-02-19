from django.urls import path
from .views import post_list,post_detail, index


urlpatterns = [
path('', index, name='index'),
path('posts/', post_list, name='post_list'),
path('posts/<int:id>', post_detail, name='post_detail'),
]