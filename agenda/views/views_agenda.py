from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from agenda.forms import FormAgendamento
from agenda.models import Agendamento, Servico


def etapa_de_agendamento(request, servico_id):
    servicos = get_object_or_404(Servico, pk=servico_id)
    return render(request, 'assets/static/crud_agenda/agendamento.html', {'servicos': servicos})

#AgendamentoCliente
def fazer_agendamento(request, servico_id):
    if request.user.is_authenticated:
        servico = get_object_or_404(Servico, pk=servico_id)
        cliente = request.user.id
        if request.method == 'POST':
            form = FormAgendamento(request.POST)
            if form.is_valid():
                profissional = form.cleaned_data['profissional']
                dia = form.cleaned_data['dia']
                horario = form.cleaned_data['horario']

                # se o dia do agendamento do cliente for igual ao dia de disponibilidade do profissional

                agendamento = Agendamento.objects.create(
                    profissional_id=profissional,
                    cliente_id=cliente,
                    servico=servico,
                    dia=dia,
                    horario=horario,
                )
                agendamento.save()
                # deixando o automovel indisponivel para não possibilitar algum clienta fazer a reserva dele
                return redirect('home')
        else:
            form = FormAgendamento()

        profissionais = User.objects.all()


        context = {
            'form': form,
            'servicos': servico
        }
        return render(request, 'assets/static/crud_agenda/agendamento.html', context)