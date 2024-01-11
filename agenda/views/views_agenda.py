from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404

from ProjectWebII.utils import group_required
from agenda.forms import FormAgendamento
from agenda.models import Agendamento, Servico


def etapa_de_agendamento(request, servico_id):
    servicos = get_object_or_404(Servico, pk=servico_id)
    return render(request, 'assets/static/crud_agenda/agendamento.html', {'servicos': servicos})

#AgendamentoFeitoPeloProfissional
@group_required(['Profissional', 'Administrador'], "/accounts/login/")
def fazer_agendamento_pelo_profissional(request):#Agendamento simples feito, falta fazer a regra de negócio
    if request.user.is_authenticated:
        #filtrandoProfissionais
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

                agendamento = Agendamento.objects.create(
                    profissional=profissional,
                    cliente=cliente,
                    dia=dia,
                    horario=horario,
                    servico=servico,
                    criado_por=criado_por,
                    criado_em=criado_em
                )
                agendamento.save()
                return redirect('home')
        else:
            form = FormAgendamento()

        context = {
            'form': form,
            'profissionais': profissionais
        }
        return render(request, 'assets/static/crud_agenda/agendamento.html', context)

@group_required(['Cliente'], "/accounts/login/")
def listar_agendamentos_cliente(request):
    agendamentos = Agendamento.objects.filter(cliente=request.user).order_by('-dia', 'horario')
    return render(request, 'assets/static/crud_agenda/agedamento_cliente/lista_agendamentos_cliente.html', {'agendamentos': agendamentos})


@group_required(['Profissional', 'Administrador'], "/accounts/login/")
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'assets/static/crud_agenda/lista_agendamentos.html', {'agendamentos': agendamentos})
