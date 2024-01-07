from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from horario.forms import AddDisponibilidade
from horario.models import Disponibilidade


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