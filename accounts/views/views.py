from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from accounts.forms import UserRegistrationForm, FormEditarUser
from django.contrib.auth.models import Group
from accounts.models import Usuario




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            user_type = form.cleaned_data.get('user_type')  # Supondo que você tenha um campo user_type no formulário
            group_name = 'Profissional' if user_type == 'profissional' else 'Cliente'
            group = Group.objects.get(name=group_name)  # Obtém o grupo correspondente
            user.groups.add(group)  # Adiciona o usuário ao grupo correspondente
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedidoio
            
            
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def minha_conta(request):
    user = request.user
    print(user)    
    context = {
        'user':user
    }

    return render(request, 'registration/minha_conta.html', context)

@login_required
def alterar_dados(request):
    user = request.user
    if request.method == 'POST':
        form = FormEditarUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('minha_conta')
    else:
        form = FormEditarUser(instance=user)

    return render(request, "registration/alterar_dados.html", {"user": user, "form": form})


@group_required(['Cliente', 'Profissional'], "/accounts/login/")
def remover_conta(request):
    usuario = get_object_or_404(Usuario, pk=request.user)
    context = {
        "usuario": usuario
    }
    return render(request, "registration/usuarios/remover_usuario.html", context)



