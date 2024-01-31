from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required, alterar_horario_atendimento
from accounts.models import Usuario
from agenda.forms import FormAgendamentoProfissional
from agenda.models import Agendamento, Servico
from horario.models import Disponibilidade, Horarios
from django.http import JsonResponse
from datetime import datetime, timedelta
def etapa_de_agendamento(request, servico_id):
    servicos = get_object_or_404(Servico, pk=servico_id)
    return render(request, 'assets/static/crud_agenda/agendamento.html', {'servicos': servicos})

# def alterar_horario_atendimento(duracao_servico, hora_atendimento):
#     # horarioAtendimento = "09:00"
#     # duracaoServico = "00:40"
#
#     # Converta os horários para objetos datetime
#     dt1 = datetime.strptime(hora_atendimento, "%H:%M")
#     dt2 = datetime.strptime(duracao_servico, "%H:%M")
#
#     # Some os horários
#     resultado = dt1 + timedelta(hours=dt2.hour, minutes=dt2.minute)
#
#     # Converta o resultado de volta para o formato de string
#     resultado = resultado.strftime("%H:%M")
#
#     print(resultado)
#     return resultado

#AgendamentoFeitoPeloProfissional
@group_required(['Profissional', 'Administrador'], "/accounts/login/")
def fazer_agendamento_pelo_profissional(request):#Agendamento simples feito, falta fazer a regra de negócio
    if request.user.is_authenticated:
        #filtrandoProfissionais
        profissional_group = Group.objects.get(name='Profissional')
        profissionais = profissional_group.user_set.all()
        if request.method == 'POST':
            form = FormAgendamentoProfissional(request.POST)
            if form.is_valid():
                profissional = form.cleaned_data['profissional']
                dia = form.cleaned_data['dia']
                horario = form.cleaned_data['horario']
                criado_por = form.cleaned_data['criado_por']
                servico = form.cleaned_data['servico']
                cliente = form.cleaned_data['cliente']

                agendamento = Agendamento.objects.create(
                    profissional=profissional,
                    cliente=cliente,
                    dia=dia,
                    horario=horario,
                    servico=servico,
                    criado_por=criado_por,
                )
                # horario_alterado = alterar_horario_atendimento(servico.janela_tempo, horario)
                # print("Horário alterado:" + horario_alterado)

                agendamento.save()
                return redirect('home')
        else:
            form = FormAgendamentoProfissional()

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


@group_required(['Cliente', 'Administrador'], "/accounts/login/")
def selecione_profissional_para_agendamento(request):
    profissionais = Usuario.objects.filter(groups__name='Profissional')

    return render(request, 'assets/static/crud_agenda/agedamento_cliente/profissional.html', {'profissionais': profissionais})

@group_required(['Cliente', 'Administrador'], "/accounts/login/")
def fazendo_agendamento_pelo_cliente(request):
    profissional_id = request.GET.get('profissional_id')
    cliente_id = request.user.id
    disponibilidades = Disponibilidade.objects.filter(profissional=profissional_id)

    if request.method == 'POST':
        dia = request.POST.get("dia")
        horario = request.POST.get("horario")
        servico_id = request.POST.get("servico")
        profissional_id_post = request.POST.get("profissional_id")

        cliente = Usuario.objects.get(pk=cliente_id)
        profissional = Usuario.objects.get(pk=profissional_id_post)
        servico_selecionado = Servico.objects.get(pk=servico_id)

        dia_selecionado = Disponibilidade.objects.get(profissional=profissional_id_post, dia=dia)
        duracao = servico_selecionado.janela_tempo

        horario_selecionado = Horarios.objects.get(disponibilidade=dia_selecionado, horario_disponivel=horario)
        if horario_selecionado:
            novo_horario_disponivel = alterar_horario_atendimento(duracao_servico=duracao, horario_atendimento=horario_selecionado)
            horario_selecionado.horario_disponivel = novo_horario_disponivel
            horario_selecionado.save()

        agendamento = Agendamento.objects.create(
            profissional=profissional,
            horario=horario,
            cliente=cliente,
            dia=dia,
            servico=servico_selecionado,
            criado_por=cliente,
        )

        agendamento.save()
        return redirect('home')

    else:
        profissional = Usuario.objects.get(pk=profissional_id)  # mostrar nome no agendamento e enviar para POST no form
        horarios = Horarios.objects.all()
        servicos = Servico.objects.all()

        context = {
            'disponibilidades': disponibilidades,#mostra os dias de expediente
            'servicos': servicos,
            'profissional': profissional,#mostra o nome do profissional selecionado
            'horarios': horarios
        }
        return render(request, 'assets/static/crud_agenda/agedamento_cliente/fazer_agendamento.html', context)




def get_horarios_disponiveis(request):
    if request.is_ajax() and request.method == 'GET':
        dia_id = request.GET.get('dia_id')
        horarios = Horarios.objects.filter(disponibilidade__dia__id=dia_id).values_list('horario_disponivel', flat=True)
        horarios_disponiveis = list(horarios)


        return JsonResponse({'horarios': horarios_disponiveis}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request'})
