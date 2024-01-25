from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required

from accounts.forms import FormEditarUser, UserProfRegistrationForm

from django.contrib.auth.models import Group
from accounts.models import Usuario

@group_required(['Administrador', 'Profissional'], "/accounts/login/")

def listar_e_cadastrar_usuarios(request):

    clientes = Usuario.objects.all()
    if request.method == 'POST':
        form = UserProfRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            user_type = form.cleaned_data.get('user_type')  # Supondo que você tenha um campo user_type no formulário
            group_name = 'Profissional' if user_type == 'profissional' else 'Cliente'
            group = Group.objects.get(name=group_name)  # Obtém o grupo correspondente
            user.groups.add(group)  # Adiciona o usuário ao grupo correspondente
            return redirect('home')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserProfRegistrationForm()

    context = {
        'clientes': clientes,
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

    return render(request, "registration/usuarios/editar_usuario.html", {"ID": usuario, "form": form})

@group_required(['Administrador'], "/accounts/login/")
def remover_usuario(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    context = {
        "usuario": usuario
    }
    return render(request, "registration/usuarios/remover_usuario.html", context)


def confirmar_remocao_usuario(request, user_id):
    Usuario.objects.get(pk=user_id).delete()

    return redirect('listar_usuarios')