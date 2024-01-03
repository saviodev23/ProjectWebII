from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from ProjectWebII.utils import group_required
from accounts.forms import UserRegistrationForm, FormEditarUser, AddDisponibilidade
from django.contrib.auth.models import Group

from accounts.models import Disponibilidade


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            user_type = form.cleaned_data.get('user_type')  # Supondo que você tenha um campo user_type no formulário
            group_name = 'Profissional' if user_type == 'profissional' else 'Cliente'
            group = Group.objects.get(name=group_name)  # Obtém o grupo correspondente
            user.groups.add(group)  # Adiciona o usuário ao grupo correspondente
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def minha_conta(request):

    return render(request, 'registration/minha_conta.html', {'user': request.user})

@login_required
def alterar_dados(request):
    user_id = request.user
    # usuario = User.objects.get(id=user_id)
    # usuario = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = FormEditarUser(request.POST, instance=user_id)

        if form.is_valid():
            form.save()
            return redirect('minha_conta')
    else:
        form = FormEditarUser(instance=user_id)

    return render(request, "registration/alterar_dados.html", {"ID": user_id, "form": form})

#CRUD de disponibilidade -- Inicio
@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def add_disponibilidade(request):
    if request.user.is_authenticated:
        disponibilidades = Disponibilidade.objects.all()
        if request.method == 'POST':
            form = AddDisponibilidade(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_disponibilidade')
        else:
            form = AddDisponibilidade()
        context = {
            'disponibilidades': disponibilidades,
            'form': form
        }

        return render(request, 'assets/static/crud_disponibilidade/add.html', context)
    else:
        return HttpResponse('erro!')

def editar_disponibilidade(request, dispo_id):
    disponibilidade = get_object_or_404(Disponibilidade, pk=dispo_id)
    if request.method == 'POST':
        form = AddDisponibilidade(request.POST, instance=disponibilidade)

        if form.is_valid():
            form.save()
            return redirect('add_disponibilidade')
    else:
        form = AddDisponibilidade(instance=disponibilidade)
    context ={
        "form": form
    }

    return render(request, "assets/static/crud_disponibilidade/editar.html", context)

def remover_disponibilidade(request, dispo_id):
    disponibilidade = get_object_or_404(Disponibilidade, pk=dispo_id)
    context = {
        "disponibilidades": disponibilidade
    }
    return render(request, "assets/static/crud_disponibilidade/remove.html", context)

def confirmar_remocao_disponibilidade(request, dispo_id):
    Disponibilidade.objects.get(pk=dispo_id).delete()

    return redirect('add_disponibilidade')


#CRUD de disponibilidade -- Fim
#adicionar depois

    # def cadastro(request):
    # if request.method == 'POST':
    #     form = CadastroForms(request.POST)
    #
    #     if form.is_valid():
    #         if form['senha'].value() != form['senha2'].value():
    #             messages.error(request, 'As senhas precisam ser iguais.')
    #             return redirect('cadastro')
    #
    #         nome = form['nome_cadastro'].value()
    #         email = form['email'].value()
    #         senha = form['senha'].value()
    #
    #         if User.objects.filter(username = nome).exists() or User.objects.filter(email = email).exists():
    #             messages.error(request, 'Email ou usuário ja cadastrado.')
    #             return redirect('cadastro')
    #
    #         usuario = User.objects.create_user(
    #             username = nome,
    #             email = email,
    #             password = senha
    #         )
    #         usuario.save()
    #         messages.success(request, f"Cadastro efetuado com sucesso!")
    #         return redirect('login')
    # else:
    #     form = CadastroForms()
    #     return render(request, 'galeria/usuarios/cadastro.html', {"form": form})
