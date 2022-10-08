from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        if not username.strip():
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('login')
        if User.objects.filter(username=username).exists():
            nome = User.objects.filter(username=username).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Logado com sucesso')
                return redirect('index')

    return render(request, 'usuarios/login.html')
