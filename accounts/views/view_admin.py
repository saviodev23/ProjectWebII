<<<<<<< HEAD
=======
from django.contrib import messages
>>>>>>> origin/savio
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from accounts.forms import FormEditarUser, UserProfRegistrationForm
from django.contrib.auth.models import Group
from accounts.models import Usuario

@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def listar_e_cadastrar_usuarios(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        form = UserProfRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data.get('user_type')  # Supondo que você tenha um campo user_type no formulário
            group_name_profissional = 'Profissional'
            group_name_secretaria = 'Secretaria'
            group_name_cliente = 'Cliente'

            if user_type == 'profissional':
                group = Group.objects.get(name=group_name_profissional)  # Obtém o grupo correspondente
                user.groups.add(group)
            elif user_type == 'secretaria':
                group = Group.objects.get(name=group_name_secretaria)
                user.groups.add(group)
            elif user_type == 'cliente':
                group = Group.objects.get(name=group_name_cliente)
                user.groups.add(group)
            else:
                return HttpResponse('grupo inválido!')
<<<<<<< HEAD

            return redirect('home')
=======
            messages.success(request, f'Usuário cadastrado com sucesso!')
            return redirect('listar_e_cadastrar_usuarios')
>>>>>>> origin/savio
    else:
        form = UserProfRegistrationForm()

    context = {
        'usuarios': usuarios,
        'form': form
    }
    return render(request, 'registration/usuarios/usuarios.html', context)
@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def editar_usuario(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)

    if request.method == 'POST':
        form = FormEditarUser(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return redirect('listar_e_cadastrar_usuarios')
    else:
        form = FormEditarUser(instance=usuario)

    context ={
        "usuario": usuario,
        "form": form
    }

    return render(request, "registration/usuarios/editar_usuario.html", context)

@group_required(['Administrador'], "/accounts/login/")
def remover_usuario(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    context = {
        "usuario": usuario
    }

    return render(request, "registration/usuarios/remover_usuario.html", context)


def confirmar_remocao_usuario(request, user_id):
<<<<<<< HEAD
    Usuario.objects.get(pk=user_id).delete()

=======
    usuario = Usuario.objects.get(pk=user_id)
    usuario.delete()
    messages.error(request, f'Usuário {usuario.username} deletado com sucesso!')
>>>>>>> origin/savio
    return redirect('listar_e_cadastrar_usuarios')