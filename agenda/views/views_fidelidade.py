from django.shortcuts import get_object_or_404, render

from ProjectWebII.utils import group_required
from accounts.models import Usuario
from agenda.models import Fidelidade, Agendamento

def resgatar_cupon(fidelidade_id, usuario_id):
    fidelidade = get_object_or_404(Fidelidade, id=fidelidade_id)
    usuario = get_object_or_404(Usuario, id=usuario_id)

    cupon = fidelidade.cupon

    cupon = cupon - 1
    usuario.desconto = 1


@group_required(['Cliente'], "/accounts/login/")
def mostrar_pontos(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    agendamentos = Agendamento.objects.filter(cliente=request.user).order_by('-dia', 'horario')
    quantidade = usuario.agendamentos_concluidos
    cupon = usuario.cupon

    context = {
        'quantidade': quantidade,
        'cupon': cupon,
        'agendamentos': agendamentos

    }
    return render(request, 'assets/static/crud_fidelidade/mostrar_pontos.html', context)


def resgatar_cupon(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    agendamentos = Agendamento.objects.filter(cliente=request.user).order_by('-dia', 'horario')
    quantidade = usuario.agendamentos_concluidos

    usuario.cupon -= 1
    usuario.desconto += 1

    usuario.save()

    cupon = usuario.cupon
    desconto = usuario.desconto

    context = {
        'quantidade': quantidade,
        'cupon': cupon,
        'agendamentos': agendamentos,
        'desconto': desconto

    }

    return render(request, "assets/static/crud_fidelidade/mostrar_pontos.html", context)


