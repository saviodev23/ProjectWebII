from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from horario.forms import AddParametro
from horario.models import Parametro

@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def add_parametro(request):
    if request.user.is_authenticated:
        profissional_group = Group.objects.get(name='Profissional')
        profissionais = profissional_group.user_set.all()
        parametros = Parametro.objects.all()

        if request.method == 'POST':
            print("teste")
            form = AddParametro(request.POST)
            print("teste2")
            if form.is_valid():
                print("test3")
                form.save()
                messages.success(request, f'Parâmetro adicionado com sucesso!')
                return redirect('add_parametro')
        else:
            form = AddParametro()
        context = {
            'parametros': parametros,
            'form': form,
            'profissionais': profissionais
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
    messages.error(request, f'Parâmetro deletado com sucesso!')
    return redirect('add_parametro')