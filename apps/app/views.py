from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForms, CommentForms, EditCommentForms
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    posts = Post.objects.order_by("publication_date")
    return render(request, 'index.html', {"cards": posts})

@login_required(login_url='login')
def buscar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'posts': posts})
    else:
        return render(request, 'search.html', {})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
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

def deletar_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    messages.success(request, 'Comentário deletado com sucesso!')
    return redirect('index')

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