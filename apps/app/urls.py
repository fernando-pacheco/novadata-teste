from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('novo-post/', views.novo_post, name='novo_post'),
    path('deletar-post/<int:post_id>', views.deletar_post, name='deletar_post'),
    path('buscar/', views.buscar, name='buscar'),
]