from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from agenda.forms import FormFidelidade
from agenda.models import Fidelidade
from django.http import HttpResponse


@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def adicionar_fidelidade(request):
    if request.user.is_authenticated:
        fidelidades = Fidelidade.objects.all()
        if request.method == 'POST':
            form = FormFidelidade(request.POST, request.FILES)
            if form.is_valid():
                #Verfificar se existe já aquele tipo de serviço cadastrado
                nome_form = form.cleaned_data['nome']
                nome_fidelidade = Fidelidade.objects.filter(nome=nome_form)
                if nome_fidelidade:
                    return HttpResponse('já existe esse serviço')

                form.save()
                return redirect('adicionar_fidelidade')
        else:
            form = FormFidelidade()
        context = {
            'fidelidades': fidelidades,
            'form': form
        }

        return render(request, 'assets/static/crud_fidelidade/cad_fidelidade.html', context)
    else:
        return HttpResponse('erro!')
    
@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def editar_fidelidade(request, fidelidade_id):
    fidelidade = get_object_or_404(Fidelidade, pk=fidelidade_id)
    if request.method == 'POST':
        form = FormFidelidade(request.POST, instance=fidelidade)

        if form.is_valid():
            form.save()
            return redirect('adicionar_fidelidade')
    else:
        form = FormFidelidade(instance=fidelidade)
    context ={
        "form": form,
        "fidelidades": fidelidade
    }


    return render(request, "assets/static/crud_Fidelidade/editar.html", context)

@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def remover_fidelidade(request, fidelidade_id):
    fidelidade = get_object_or_404(Fidelidade, pk=fidelidade_id)
    context = {
        "fidelidade": fidelidade
    }
    return render(request, "assets/static/crud_Fidelidade/remove.html", context)


def confirmar_remocao_fidelidade(request, fidelidade_id):
    Fidelidade.objects.get(pk=fidelidade_id).delete()

    return redirect('adicionar_fidelidade')