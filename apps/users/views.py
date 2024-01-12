from django.shortcuts import render, redirect
from apps.users.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    '''Criação do formulário de login'''
    form = LoginForms()

    # Verifica se o formulário foi enviado
    if request.method == 'POST':
        form = LoginForms(request.POST)

        # Verifica se o formulário foi preenchido corretamente
        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        # Verifica se o usuário existe
        user = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        # Verifica se o usuário existe
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{nome} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request,'Erro ao efetuar o login')
            return redirect('login')

    return render(request, 'users/login.html', {"form": form})


def cadastro(request):
    '''Criação do formulário de cadastro'''
    cadastro = CadastroForms()

    # Verifica se o formulário foi enviado
    if request.method == 'POST':
        cadastro = CadastroForms(request.POST)

        # Verifica se o formulário foi preenchido corretamente
        if cadastro.is_valid():            
            nome = cadastro['nome_cadastro'].value()
            email = cadastro['email'].value()
            senha = cadastro['senha_1'].value()

            # Verifica se o nome de login existe
            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já existe')
                return redirect('cadastro')
            
            # Criação do usuário
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            
            # Salva o usuário
            user.save()
            messages.success(request,'Usuário cadastrado com sucesso')
            return redirect('login')

    return render(request, 'users/cadastro.html', {"cadastro":cadastro})

def logout(request):
    '''Criação do formulário de logout'''
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    return redirect(login)