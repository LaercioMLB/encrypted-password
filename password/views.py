from django.shortcuts import render,redirect
from .controller import EncriptyPassword, DescriptyPassword
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Password
from .forms import PasswordForm

def lista_password(request):
    context = {}
    context['passwords'] = Password.objects.all()
    return render(request, './dash/dashboard.html', context)

def create_new_password(request):
    context = {'form': PasswordForm(request.POST or None)}

    if request.method == "POST":
        if context['form'].is_valid():
            pass_hash, key = EncriptyPassword(context['form'].cleaned_data['senha'])
            Password.objects.create(
                senha = pass_hash,
                username = context['form'].cleaned_data['username'],
                descricao = context['form'].cleaned_data['descricao'],
                url = context['form'].cleaned_data['url'],
                key = key,
            )
        return redirect('index')

def view_password(request):
    if request.method == "POST":
        senha = Password.objects.get(id=request.POST['id_senha'])
        password = {
            'id': senha.id,
            'url': senha.url,
            'descricao': senha.descricao,
            'username': senha.username,
            'senha': DescriptyPassword(senha.senha, senha.key),
        }
        return JsonResponse(password)

def update_password(request):
    context = {'form': PasswordForm(request.POST or None)}

    if request.method == "POST":
        if context['form'].is_valid():
            senha = Password.objects.get(id=request.POST['id_senha'])
            pass_hash, key = EncriptyPassword(context['form'].cleaned_data['senha'])

            senha.senha = pass_hash
            senha.username = context['form'].cleaned_data['username']
            senha.descricao = context['form'].cleaned_data['descricao']
            senha.url = context['form'].cleaned_data['url']
            senha.key = key
            senha.save()
            
        return redirect('index')

def delete_password(request):
    if request.method == "POST":
        Password.objects.get(id=request.POST['id_senha']).delete()
        return HttpResponseRedirect(reverse('index'))
