
# Novadata - Teste

Resolução do teste técnico para a vaga de Desenvolvedor Python - Django


## Pré-requisitos

- Python 3.12.x


## Instalação

Para criar o ambiente virtual
```bash
  python -m venv env
```

Em seguida, ative o ambiente
```bash
  .\env\Scripts\activate
```

Após ativado, instale as dependências em requirements.txt
```bash
  pip install -r requirements.txt
```

Realize as migrações pendentes
```bash
  python manage.py makemigrations
  python manage.py migrate
```

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

*Crie um arquivo com nome .env na raíz do projeto*

`SECRET_KEY` = django-insecure-nvi12p!=s8w!49pf@5iw!@6a#r-t(i00q^xl=@rwg4&bnqqrd+


Por fim, suba o servidor local
```bash
  python manage.py runserver
```
## Uso - Rotas

rotas: 
    (localhost:8000/api) - API Root DRF | (localhost:8000/app) - Aplicação

Em localhost:8000/app será necessário realizar o cadastro do usuário para entrar na página principal de posts e realizar o cadastro deles. Um usuário pode realizar o post/comentário, editar, ou deletar, desde que seja de sua autoria.

## Rota - admin

Utilizei o honeypot para realizar tratamentos de segurança na aplicação, então a rota para acessar a área de admin do Django: localhost:8000/area-restrita/
