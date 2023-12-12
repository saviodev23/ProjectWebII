from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from agenda.forms import FormAddServico
from agenda.models import Servico

@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def add_servico(request):
    if request.user.is_authenticated:
        servicos = Servico.objects.all()
        if request.method == 'POST':
            form = FormAddServico(request.POST)
            if form.is_valid():
                #Verfificar se existe já aquele tipo de serviço cadastrado
                nome_form = form.cleaned_data['nome_servico']
                nome_servico = Servico.objects.filter(nome_servico=nome_form)
                if nome_servico:
                    return HttpResponse('já existe esse serviço')

                form.save()
                return redirect('add_servico')
        else:
            form = FormAddServico()
        context = {
            'servicos': servicos,
            'form': form
        }

        return render(request, 'assets/static/crud_servico/add.html', context)
    else:
        return HttpResponse('erro!')
@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def editar_servico(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    if request.method == 'POST':
        form = FormAddServico(request.POST, instance=servico)

        if form.is_valid():
            form.save()
            return redirect('add_servico')
    else:
        form = FormAddServico(instance=servico)
    context ={
        "form": form,
        "servicos": servico
    }

    return render(request, "assets/static/crud_servico/editar.html", context)

@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def remover_servico(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    context = {
        "servico": servico
    }
    return render(request, "assets/static/crud_servico/remove.html", context)

def confirmar_remocao_servico(request, servico_id):
    Servico.objects.get(pk=servico_id).delete()

    return redirect('add_servico')