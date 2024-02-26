from datetime import datetime, timedelta

def alterar_horario_atendimento(duracao_servico, horario_atendimento):
    # horarioAtendimento = "09:00"
    # duracaoServico = "00:40"

    # Converta os horários para objetos datetime
    horaAtendimento = datetime.strptime(horario_atendimento, "%H:%M")
    duracaoServico = datetime.strptime(duracao_servico, "%H:%M")

    # Some os horários
    resultado = horaAtendimento + timedelta(hours=duracaoServico.hour, minutes=duracaoServico.minute)

    # Converta o resultado de volta para o formato de string
    resultado = resultado.strftime("%H:%M")

    return resultado


resultado = alterar_horario_atendimento("00:40", "06:00")
print(resultado)


# -----------------------------------------
# horario_selecionado = Horarios.objects.get(pk=horario)

duracao_servico = servico_selecionado.janela_tempo

# Converta o horário de atendimento para objeto time
horario_convertido = datetime.strptime(horario, "%H:%M").time()

    horario_alterado = alterar_horario_atendimento(duracao_servico, horario_convertido)
    print(horario_alterado)
    try:
        horario_obj = Horarios.objects.get(disponibilidade__profissional=profissional,
                                           horario_disponivel=horario_convertido)
        horario_obj.horario_disponivel = horario_alterado
        horario_obj.save()

    except Horarios.DoesNotExist:
        return HttpResponse('objeto NONE')

# Converte horario_disponivel para datetime.datetime
horario_datetime = datetime.combine(datetime.today(), horario_selecionado.horario_disponivel)

# Adiciona a duracao
horario_datetime += timedelta(minutes=duracao.minute, seconds=duracao.second)

# Converte de volta para datetime.time
novo_horario_disponivel = horario_datetime.time()

# Atualiza o horario_disponivel
horario_selecionado.horario_disponivel = novo_horario_disponivel
horario_selecionado.save()