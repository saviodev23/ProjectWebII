from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.models import Usuario
from horario.models import Disponibilidade, Parametro, Horarios
from datetime import datetime, timedelta

def gerar_horarios_disponiveis(request, profissional_id):
    disponibilidades = Disponibilidade.objects.filter(profissional=profissional_id)

    for disponibilidade in disponibilidades:
        # Calcula os horários disponíveis para cada disponibilidade
        horarios_disponiveis_disponibilidade = calcular_horarios_disponiveis(disponibilidade)

        for horario_disponivel in horarios_disponiveis_disponibilidade:
            # Verifica se já existe um registro para essa combinação
            if not Horarios.objects.filter(disponibilidade=disponibilidade,
                                           horario_disponivel=horario_disponivel).exists():
                # Cria um registro Horarios para cada horário disponível
                horarios = Horarios.objects.create(
                    disponibilidade=disponibilidade,
                    horario_disponivel=horario_disponivel
                )
                horarios.save()
            else:
                messages.warning(request, 'Os horários deste profissional já estão gerados.')
                return redirect('listar_horarios')

    messages.success(request, f'Horários de {disponibilidade.profissional} gerados com sucesso!')
    return redirect('listar_horarios')

def calcular_horarios_disponiveis(disponibilidade):
    horario_inicio = datetime.combine(datetime.today(), disponibilidade.horario_inicio)
    horario_fim = datetime.combine(datetime.today(), disponibilidade.horario_fim)
    ciclo_servico = Parametro.objects.get(criado_por=disponibilidade.profissional).valor

    horarios_disponiveis = []

    horario_atual = horario_inicio
    while horario_atual <= horario_fim:
        # Exclui horários entre 12:00 e 14:00
        if horario_atual.time() <= datetime.strptime("12:00", "%H:%M").time() \
                or horario_atual.time() >= datetime.strptime("14:00", "%H:%M").time():
            horarios_disponiveis.append(horario_atual.strftime("%H:%M"))

        horario_atual += timedelta(minutes=ciclo_servico)

    return horarios_disponiveis


def listar_horarios(request):
    horarios = Horarios.objects.all()

    # filtrandoProfissionais
    profissional_group = Group.objects.get(name='Profissional')
    profissionais = profissional_group.user_set.all()

    context = {
        'horarios': horarios,
        'profissionais': profissionais,
        # 'horarios_filtrados': horarios_filtrados
    }
    return render(request, 'assets/static/horarios/visualizar_horarios.html', context)

def apagar_horarios_disponiveis(request, profissional_id):
    profissional = Usuario.objects.get(pk=profissional_id)
    context ={
        'profissional': profissional
    }
    return render(request, 'assets/static/horarios/remove.html', context)

def confirmar_remocao_horarios(request, profissional_id):
    profissional = Usuario.objects.get(id=profissional_id)
    horarios = Horarios.objects.filter(disponibilidade__profissional=profissional_id)
    if horarios.exists():
        horarios.delete()
        messages.error(request, f'Horários apagados com sucesso!')
    else:
        messages.warning(request, f'Os horários de {profissional.username} já foram deletados!')
    return redirect('listar_horarios')

def buscar_horarios(request):
    query = request.GET.get('q')
    horarios = Horarios.objects.filter(disponibilidade__profissional__username__icontains=query)
    return render(request, 'assets/static/horarios/visualizar_horarios.html', {'horarios': horarios})


