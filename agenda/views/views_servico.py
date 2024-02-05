from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from agenda.forms import FormAddServico, ImagemServicoForm
from agenda.models import Servico, ImagemServico


@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def add_servico(request):
    if request.user.is_authenticated:
        servicos = Servico.objects.all()
        if request.method == 'POST':
            form = FormAddServico(request.POST)
            if form.is_valid():
                #Verfificar se existe já aquele tipo de serviço cadastrado
                nome_form = form.cleaned_data['nome']
                nome_servico = Servico.objects.filter(nome=nome_form)
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

def detalhes_servico(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    imagens_servico = ImagemServico.objects.filter(servico=servico_id)

    context ={
        'servico': servico,
        'imagens_servico': imagens_servico
    }
    return render(request, 'assets/static/crud_servico/servico.html', context)

#CRUD Imagem Servico
def add_imagem_servico(request):
    if request.user.is_authenticated:
        imagens_servicos = ImagemServico.objects.all()
        if request.method == 'POST':
            form = ImagemServicoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('add_imagem_servico')
        else:
            form = ImagemServicoForm()
        context = {
            'imagens_servicos': imagens_servicos,
            'form': form
        }

        return render(request, 'assets/static/crud_servico/imagem_servico/add.html', context)
    else:
        return HttpResponse('erro!')

@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def editar_imagem_servico(request, img_servico_id):
    imagem_servico = get_object_or_404(ImagemServico, pk=img_servico_id)
    if request.method == 'POST':
        form = ImagemServicoForm(request.POST, request.FILES, instance=imagem_servico)

        if form.is_valid():
            form.save()
            return redirect('add_imagem_servico')
    else:
        form = ImagemServicoForm(instance=imagem_servico)
    context ={
        "form": form,
        "imagem_servico": imagem_servico
    }

    return render(request, "assets/static/crud_servico/imagem_servico/editar.html", context)
@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def remover_imagem_servico(request, img_servico_id):
    imagem_servico = get_object_or_404(ImagemServico, pk=img_servico_id)
    context = {
        "imagem_servico": imagem_servico
    }
    return render(request, "assets/static/crud_servico/imagem_servico/remove.html", context)
def confirmar_remocao_imagem_servico(request, img_servico_id):
    ImagemServico.objects.get(pk=img_servico_id).delete()

    return redirect('add_imagem_servico')