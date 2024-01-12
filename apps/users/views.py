from django.shortcuts import render, redirect
from apps.users.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        user = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{nome} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request,'Erro ao efetuar o login')
            return redirect('login')

    return render(request, 'users/login.html', {"form": form})


def cadastro(request):
    cadastro = CadastroForms()

    if request.method == 'POST':
        cadastro = CadastroForms(request.POST)

        if cadastro.is_valid():
            
            
            nome = cadastro['nome_cadastro'].value()
            email = cadastro['email'].value()
            senha = cadastro['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já existe')
                return redirect('cadastro')
            
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            user.save()
            messages.success(request,'Usuário cadastrado com sucesso')
            return redirect('login')

    return render(request, 'users/cadastro.html', {"cadastro":cadastro})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')

    return redirect(login)