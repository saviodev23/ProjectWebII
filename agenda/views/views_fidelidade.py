from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from ProjectWebII.utils import group_required
from accounts.models import Usuario
from agenda.forms import FormFidelidade
from agenda.models import Fidelidade, Agendamento, Servico
from django.contrib import messages

def listar_planos_fidelidade(request):
    fidelidades = Fidelidade.objects.all()
    context = {
        'fidelidades': fidelidades
    }
    return render(request, 'assets/static/crud_fidelidade/fidelidade.html', context)

#CRUD
@group_required(['Administrador', 'Profissional', 'Secretaria'], "/accounts/login/")
def adicionar_fidelidade(request):
    if request.user.is_authenticated:
        fidelidades = Fidelidade.objects.all()
        if request.method == 'POST':
            form = FormFidelidade(request.POST, request.FILES)
            if form.is_valid():
                # Verfificar se existe já aquele tipo de serviço cadastrado
                nome_form = form.cleaned_data['nome']
                nome_fidelidade = Fidelidade.objects.filter(nome=nome_form)
                if nome_fidelidade:
                    messages.warning(request, f'Essa Fidelidade já existe no sistema!')

                messages.success(request, f'Fidelidade cadastrada com sucesso!')
                form.save()
                return redirect('adicionar_fidelidade')
        else:
            form = FormFidelidade()
        context = {
            'fidelidades': fidelidades,
            'form': form
        }

        return render(request, 'assets/static/crud_fidelidade/add.html', context)
    else:
        return HttpResponse('erro!')


@group_required(['Administrador', 'Profissional', 'Secretaria'], "/accounts/login/")
def editar_fidelidade(request, fidelidade_id):
    fidelidade = get_object_or_404(Fidelidade, pk=fidelidade_id)
    if request.method == 'POST':
        form = FormFidelidade(request.POST, instance=fidelidade)

        if form.is_valid():
            form.save()
            messages.success(request, f'Fidelidade editada com sucesso!')
            return redirect('adicionar_fidelidade')
    else:
        form = FormFidelidade(instance=fidelidade)
    context = {
        "form": form,
        "fidelidades": fidelidade
    }

    return render(request, "assets/static/crud_Fidelidade/editar.html", context)


@group_required(['Administrador', 'Profissional', 'Secretaria'], "/accounts/login/")
def remover_fidelidade(request, fidelidade_id):
    fidelidade = get_object_or_404(Fidelidade, pk=fidelidade_id)
    context = {
        "fidelidade": fidelidade
    }
    return render(request, "assets/static/crud_Fidelidade/remove.html", context)


def confirmar_remocao_fidelidade(request, fidelidade_id):
    Fidelidade.objects.get(pk=fidelidade_id).delete()
    messages.error(request, f'Fidelidade deletada com sucesso!')
    return redirect('adicionar_fidelidade')

#CRUD - FIM

@group_required(['Cliente', 'Administrador'], "/accounts/login/")
def resgatar_fidelidade(request, fidelidade_id):
    usuario = request.user
    fidelidade = get_object_or_404(Fidelidade, pk=fidelidade_id)
    usuario.fidelidade = fidelidade
    usuario.save()
    if usuario.fidelidade is not None:
        messages.success(request, f'Plano de fidelidade resgatado com sucesso!')
        return redirect('home')
    if usuario.fidelidade:
        messages.warning(request, f'Plano de fidelidade já resgatado!')
        return redirect('home')

    servicos = Servico.objects.all()
    fidelidades = Fidelidade.objects.all()
    context = {
        'servicos': servicos,
        'fidelidades': fidelidades
    }

    return render(request, 'assets/static/crud_fidelidade/fidelidade.html', context)


@group_required(['Cliente', 'Administrador'], "/accounts/login/")
def mostrar_pontos(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    agendamentos = Agendamento.objects.filter(cliente=request.user, status_agendamento='CO').order_by('-dia', 'horario')
    fidelidade = usuario.fidelidade
    desconto = usuario.desconto
    quantidade = agendamentos.count()
    context = {
        'fidelidade': fidelidade,
        'desconto': desconto

    }
    if hasattr(usuario, 'fidelidade') and usuario.fidelidade:
        valor = quantidade % fidelidade.requisito
        desconto = usuario.desconto
        falta = fidelidade.requisito - valor

        context = {
            'fidelidade': fidelidade,
            'desconto': desconto,
            'falta': falta,
        }
    return render(request, 'assets/static/crud_Fidelidade/mostrar_pontos.html', context)

@group_required(['Cliente', 'Administrador'], "/accounts/login/")
def remover_fidelidade_cliente(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    usuario.fidelidade = None
    usuario.save()

    if usuario.fidelidade == None:
        messages.error(request, f'Fidelidade removida com sucesso!')

    return redirect('mostrar_pontos', user_id=user_id)