from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from horario.forms import AddDisponibilidade, AddParametro
from horario.models import Disponibilidade, Parametro

#CRUD de disponibilidade -- Inicio
@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def add_disponibilidade(request):
    if request.user.is_authenticated:
        #filtrandoProfissionais
        profissional_group = Group.objects.get(name='Profissional')
        profissionais = profissional_group.user_set.all()
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
            'form': form,
            'profissionais': profissionais
        }

        return render(request, 'assets/static/crud_disponibilidade/add.html', context)
    else:
        return HttpResponse('erro!')

def editar_disponibilidade(request, dispo_id):
    # filtrandoProfissionais
    profissional_group = Group.objects.get(name='Profissional')
    profissionais = profissional_group.user_set.all()
    disponibilidade = get_object_or_404(Disponibilidade, pk=dispo_id)
    if request.method == 'POST':
        form = AddDisponibilidade(request.POST, instance=disponibilidade)

        if form.is_valid():
            form.save()
            return redirect('add_disponibilidade')
    else:
        form = AddDisponibilidade(instance=disponibilidade)
    context ={
        "form": form,
        "profissionais":profissionais
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

#CRUD de Parametros
@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def add_parametro(request):
    if request.user.is_authenticated:
        parametro = Parametro.objects.all()
        if request.method == 'POST':
            form = AddParametro(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_parametro')
        else:
            form = AddParametro()
        context = {
            'parametros': parametro,
            'form': form
        }

        return render(request, 'assets/static/crud_parametro/add.html', context)
    else:
        return HttpResponse('erro!')

def editar_parametro(request, parametro_id):
    parametro = get_object_or_404(Parametro, pk=parametro_id)
    if request.method == 'POST':
        form = AddParametro(request.POST, instance=parametro)

        if form.is_valid():
            form.save()
            return redirect('add_parametro')
    else:
        form = AddParametro(instance=parametro)
    context ={
        "form": form
    }

    return render(request, "assets/static/crud_parametro/editar.html", context)

def remover_parametro(request, parametro_id):
    parametro = get_object_or_404(Parametro, pk=parametro_id)
    context = {
        "parametros": parametro
    }
    return render(request, "assets/static/crud_parametro/remove.html", context)

def confirmar_remocao_parametro(request, parametro_id):
    Parametro.objects.get(pk=parametro_id).delete()

    return redirect('add_parametro')

#CRUD de parametros FIM