from django.shortcuts import render, redirect, get_object_or_404
from agenda.forms import FormAgendamento
from agenda.models import Agendamento


def fazer_agendamento(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FormAgendamento(request.POST)
            if form.is_valid():
                profissional = form.cleaned_data['profissional']
                cliente = form.cleaned_data['cliente']
                servico = form.cleaned_data['servico']
                dia = form.cleaned_data['dia']
                horario = form.cleaned_data['horario']
                status_agendamento = form.cleaned_data['status_agendamento']

                #fazer a regra de negócio aqui

                agendamento = Agendamento.objects.create(
                    profissional_id=profissional,
                    cliente_id=cliente,
                    servico=servico,
                    dia=dia,
                    horario=horario,
                    status_agendamento=status_agendamento,
                )
                agendamento.save()
                # deixando o automovel indisponivel para não possibilitar algum clienta fazer a reserva dele
                return redirect('home')
        else:
            form = FormAdminLocacao()

        clientes = User.objects.all()

        context = {
            'form': form,
            'clientes': clientes
        }
        return render(request, 'assets/locacao_admins/add_locacao.html', context)