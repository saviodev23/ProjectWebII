from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Usuario
from ProjectWebII.utils import group_required
from agenda.forms import FormAgendamento, FormEditarAgendamento
from agenda.models import Agendamento, Servico, Fidelidade
from decimal import Decimal




def etapa_de_agendamento(request, servico_id):
    servicos = get_object_or_404(Servico, pk=servico_id)
    return render(request, 'assets/static/crud_agenda/agendamento.html', {'servicos': servicos})

#AgendamentoFeitoPeloProfissional
@group_required(['Profissional', 'Administrador'], "/accounts/login/")
def fazer_agendamento_pelo_profissional(request):
    #Agendamento simples feito, falta fazer a regra de negócio
    if request.user.is_authenticated:
        #filtrandoProfissionais
        
       #usuario = get_object_or_404(Usuario, id=usuario_id)
        profissional_group = Group.objects.get(name='Profissional')
        profissionais = profissional_group.user_set.all()
       

        if request.method == 'POST':
            form = FormAgendamento(request.POST)
            if form.is_valid():
                profissional = form.cleaned_data['profissional']
                dia = form.cleaned_data['dia']
                horario = form.cleaned_data['horario']
                criado_por = form.cleaned_data['criado_por']
                servico = form.cleaned_data['servico']
                criado_em = form.cleaned_data['criado_em']
                cliente = form.cleaned_data['cliente']
                   
                preco = servico.preco
                usuario = cliente

                if usuario.desconto == 1:

                     preco = Decimal(float(preco) * 0.5)
                
                
                agendamento = Agendamento.objects.create(
                   
                    profissional=profissional,
                    cliente=cliente,
                    dia=dia,
                    horario=horario,
                    servico=servico,
                    preco_servico=preco,
                    criado_por=criado_por,
                    criado_em=criado_em
                )
                agendamento.save()
                return redirect('home')
        else:
            form = FormAgendamento()

        context = {
            'form': form,
            'profissionais': profissionais,
        }
        return render(request, 'assets/static/crud_agenda/agendamento.html', context)

@group_required(['Cliente'], "/accounts/login/")
def listar_agendamentos_cliente(request):
    agendamentos = Agendamento.objects.filter(cliente=request.user).order_by('-dia', 'horario')
    return render(request, 'assets/static/crud_agenda/agendamento_cliente/lista_agendamentos_cliente.html', {'agendamentos': agendamentos})


@group_required(['Profissional', 'Administrador'], "/accounts/login/")
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'assets/static/crud_agenda/lista_agendamentos.html', {'agendamentos': agendamentos})

@group_required(['Administrador', 'Profissional'], "/accounts/login/")
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)

    if request.method == 'POST':
        form = FormEditarAgendamento(request.POST, instance=agendamento)

        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else:
        form = FormEditarAgendamento(instance=agendamento)

    return render(request, "assets/static/crud_agenda/agendamento_cliente/editar_agendamentos", {"ID": agendamento, "form": form})


def concluir_agendamento(request, agendamento_id):
    agendamentos = Agendamento.objects.all()
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    usuario = agendamento.cliente

    if agendamento.status_agendamento == 'AG':
        agendamento.status_agendamento = 'CO'
        usuario.agendamentos_concluidos += 1
         
        agendamento.save()
        usuario.save()
      
        if usuario.agendamentos_concluidos % 5 == 0:
            usuario.cupon +=1
        
            usuario.save()

    context = {
        'agendamento': agendamento,
        'agendamentos': agendamentos
    }

    return render(request, "assets/static/crud_agenda/lista_agendamentos.html", context)





