from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForms, CommentForms, EditCommentForms
from django.contrib import messages
from django.core.cache import cache

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    posts = cache.get('posts')
    if not posts:
        posts = Post.objects.order_by("publication_date")
        cache.set('posts', posts, 5)

    return render(request, 'index.html', {'cards': posts})

@login_required(login_url='login')
def buscar(request):
    if request.method == 'POST':
        busca = request.POST['busca']
        posts = Post.objects.filter(title__contains=busca)
        return render(request, 'busca.html', {'buscado': busca, 'posts': posts})
    else:
        return render(request, 'busca.html', {})

def post(request, post_id):
    post = get_object_or_404(Post.objects.select_related('author'), pk=post_id)
    comments = Comment.objects.filter(post=post).select_related('author')
    return render(request, 'post.html', {'post': post, 'comments': comments})

def novo_post(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    form = PostForms

    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Novo POST publicado!')
            return redirect('index')

    return render(request, 'novo_post.html', {'form': form})

def deletar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'Post deletado com sucesso!')
    return redirect('index')

def filtro(request):
    posts = Post.objects.order_by("publication_date")
    return render(request, 'index.html', {'card':posts})

def deletar_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.success(request, 'Comentário deletado com sucesso!')
        return redirect('post', post_id=post_id)
    else:
        messages.error(request, 'Você não tem permissão para excluir este comentário.')
        return redirect('post', post_id=post_id)

def editar_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    form = EditCommentForms(instance=comment)
    if request.method == 'POST':
        form = EditCommentForms(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentário editado com sucesso!')
            return redirect('post', post_id=post_id)
    return render(request, 'editar_comment.html', {'form': form, 'comment': comment})

def novo_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForms()
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comentário publicado!')
            return redirect('post', post_id=post_id)
    return render(request, 'post.html', {'form': form, 'post': post, 'comments': comments})