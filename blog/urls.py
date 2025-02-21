from django.urls import path
from .views import post_list,post_detail, index, blog, ajout_post



urlpatterns = [
path('blog/', blog, name='blog'),   
path('', index, name='index'),
path('posts/', post_list, name='post_list'),
path('posts/<int:id>', post_detail, name='post_detail'),
path('form/',ajout_post, name='formulaire'),
]