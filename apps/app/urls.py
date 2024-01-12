from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('novo-post/', views.novo_post, name='novo_post'),
    path('deletar-post/<int:post_id>', views.deletar_post, name='deletar_post'),
    path('post/<int:post_id>/deletar_comment/<int:comment_id>/', views.deletar_comment, name='deletar_comment'),
    path('post/<int:post_id>/editar_comment/<int:comment_id>/', views.editar_comment, name='editar_comment'),
    path('buscar/', views.buscar, name='buscar'),
    path('post/<int:post_id>/comment/', views.novo_comment, name='novo_comment'),
]