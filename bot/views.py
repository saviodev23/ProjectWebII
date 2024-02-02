from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime, timedelta as td
from agenda.forms import FormAgendamentoCliente

@csrf_exempt
def bot(request):   
    user_message = request.POST.get('Body', '').lower()
    horarios_disponiveis = gerar_horarios_disponiveis()


    # Verificar se o usuário está solicitando os horários disponíveis
    if user_message == 'horarios':
        response_message = f"Horários disponíveis:\n{formatar_horarios(horarios_disponiveis)}"
    # Verificar se o usuário está tentando reservar um horário
    elif user_message.startswith('reservar'):
        horario_reservado = user_message.replace('reservar ', '').strip()
        response_message = reservar_horario(horario_reservado, horarios_disponiveis.copy())
    else:
        # Se a mensagem do usuário não corresponder a nenhuma das opções acima, solicite as informações para agendamento
        response_message = "Olá! Para agendar um horário, por favor, forneça as seguintes informações:\n- Dia desejado (DD/MM/AAAA)\n- Horário desejado (HH:MM)\n- Serviço desejado"

    # Construir a resposta
    twilio_response = MessagingResponse()
    twilio_response.message(response_message)

    return HttpResponse(str(twilio_response))
    
def gerar_horarios_disponiveis():
    horario_inicio = datetime.strptime("08:00", "%H:%M")
    horario_final = datetime.strptime("18:00", "%H:%M")
    intervalo = td(minutes=30)

    horarios_disponiveis = []
    horario_atual = horario_inicio

    while horario_atual < horario_final:
        # Exclui horários entre 12:00 e 14:00
        if horario_atual.time() < datetime.strptime("12:00", "%H:%M").time() or \
                horario_atual.time() >= datetime.strptime("14:00", "%H:%M").time():
            horarios_disponiveis.append(horario_atual.strftime("%H:%M"))
        horario_atual += intervalo

    return horarios_disponiveis

def formatar_horarios(horarios):
    formatted_horarios = ""
    for i, horario in enumerate(horarios, start=1):
        formatted_horarios += f"{i}. {horario}\n"
    return formatted_horarios


def processar_mensagem(request):
    if request.method == 'POST':
        form = FormAgendamentoCliente(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Agendamento realizado com sucesso!")
    else:
        form = FormAgendamentoCliente()
    return render(request, 'agendamento.html', {'form': form})


def reservar_horario(horario_reservado, horarios_disponiveis):
    if horario_reservado.isdigit() and 1 <= int(horario_reservado) <= len(horarios_disponiveis):
        horario_selecionado = horarios_disponiveis[int(horario_reservado) - 1]
        horarios_disponiveis.remove(horario_selecionado)
        return f"Horário {horario_selecionado} reservado com sucesso!"
    else:
        return "Por favor, forneça um número válido correspondente ao horário desejado."

def enviar_mensagem(destinatario, mensagem):
    # Configurar as credenciais do Twilio
    account_sid = 'ACb079459447497a6a92e585083c1d4c7a'
    auth_token = '2b07f7c0995fceea65b5e5074ff6936e'
    client = Client(account_sid, auth_token)

    # Enviar a mensagem
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=mensagem,
        to=destinatario
    )


