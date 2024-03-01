from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from ProjectWebII.utils import group_required
from accounts.models import Usuario
from agenda.forms import FormAgendamentoProfissional, FormEditarAgendamento
from agenda.models import Agendamento, Servico
from horario.models import Disponibilidade, Horarios, Parametro
from datetime import datetime, timedelta
from django.contrib import messages
from decimal import Decimal

@group_required(['Profissional', 'Administrador', 'Secretaria'], "/accounts/login/")
def fazer_agendamento_pelo_profissional(request):
    # Agendamento simples feito, falta fazer a regra de negócio
    if request.user.is_authenticated:
        # filtrandoProfissionais

        # usuario = get_object_or_404(Usuario, id=usuario_id)
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

                preco = servico.preco
                usuario = cliente

                fidelidade = usuario.fidelidade

                if usuario.fidelidade is not None:
                    if usuario.desconto > 0:
                        desconto = preco * (fidelidade.desconto / Decimal('100'))
                        preco = preco - desconto
                        usuario.desconto = 0

            agendamento = Agendamento.objects.create(
                profissional=profissional,
                cliente=cliente,
                dia=dia,
                horario=horario,
                servico=servico,
                preco_servico=preco,
                criado_por=criado_por,
            )
            agendamento.save()
            usuario.save()
            messages.success(request, f'Agendamento de horário realizado com sucesso!')
            return redirect('home')
        else:
            form = FormAgendamentoProfissional()

        context = {
            'form': form,
            'profissionais': profissionais,
        }
        return render(request, 'assets/static/crud_agenda/agendamento.html', context)

@group_required(['Administrador', 'Profissional', 'Secretaria'], "/accounts/login/")
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)

    if request.method == 'POST':
        form = FormEditarAgendamento(request.POST, instance=agendamento)

        if form.is_valid():
            form.save()
            messages.success(request, f'Agendamento editado com sucesso!')
            return redirect('listar_agendamentos')
    else:
        form = FormEditarAgendamento(instance=agendamento)

    return render(request, "assets/static/crud_agenda/editar_agendamento.html", {"ID": agendamento, "form": form})


@group_required(['Cliente', 'Administrador'], "/accounts/login/")
def listar_agendamentos_cliente(request):
    agendamentos = Agendamento.objects.filter(cliente=request.user).order_by('status_agendamento')
    context = {
        'agendamentos': agendamentos
    }
    return render(request, 'assets/static/crud_agenda/agedamento_cliente/lista_agendamentos_cliente.html', context)


@group_required(['Profissional', 'Administrador', 'Secretaria'], "/accounts/login/")
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('status_agendamento')
    context = {
        'agendamentos': agendamentos
    }
    return render(request, 'assets/static/crud_agenda/lista_agendamentos.html', context)

def buscar_agendamentos(request):
    query = request.GET.get('q')
    agendamentos = Agendamento.objects.filter(cliente__username__icontains=query) | Agendamento.objects.filter(profissional__username__icontains=query)
    return render(request, 'assets/static/crud_agenda/lista_agendamentos.html', {'agendamentos': agendamentos})

@group_required(['Cliente', 'Administrador'], "/accounts/login/")
def selecione_profissional_para_agendamento(request):
    profissionais = Usuario.objects.filter(groups__name='Profissional')

    return render(request, 'assets/static/crud_agenda/agedamento_cliente/profissional.html', {'profissionais': profissionais})

@group_required(['Cliente', 'Administrador'], "/accounts/login/")
def fazer_agendamento_pelo_cliente(request):
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
        duracao_servico = servico_selecionado.janela_tempo

        horario_selecionado_para_agenda = Horarios.objects.get(disponibilidade=dia_selecionado, horario_disponivel=horario)

        valor_paramentro = Parametro.objects.get(criado_por=profissional).valor
        horarios = Horarios.objects.filter(disponibilidade__profissional=profissional, disponibilidade=dia_selecionado)
        horario_agendado = Agendamento.horario

        if horario_selecionado_para_agenda:
            if horario_selecionado_para_agenda.horario_disponivel != horario_agendado:
                novo_horario_disponivel = alterar_horario_atendimento(duracao_servico=duracao_servico, horario_atendimento=horario_selecionado_para_agenda)
                horario_selecionado_para_agenda.horario_disponivel = novo_horario_disponivel
                horario_selecionado_para_agenda.save()

                # Atualiza os horários subsequentes
                horario_agendamento = novo_horario_disponivel
                for hora in horarios:
                    if hora.horario_disponivel != horario_agendamento:
                        novo_horario_atualizado = (datetime.combine(datetime.today(), hora.horario_disponivel) + timedelta(
                            minutes=valor_paramentro)).time()

                        hora.horario_disponivel = novo_horario_atualizado
                        hora.save()
            else:
                messages.warning(request, f'Esse horário já está agendado')
                return redirect('fazendo_agendamento_pelo_cliente')

        else:
            messages.warning(request, f'Horário ou dia incompátiveis, tente novamente.')
            return redirect('home')

        preco = servico_selecionado.preco
        usuario = cliente

        fidelidade = usuario.fidelidade

        if usuario.fidelidade is not None:
            if usuario.desconto > 0:
                desconto = preco * (fidelidade.desconto / Decimal('100'))
                preco = preco - desconto
                usuario.desconto = 0

        agendamento = Agendamento.objects.create(
            profissional=profissional,
            horario=horario,
            cliente=cliente,
            dia=dia,
            servico=servico_selecionado,
            preco_servico=preco,
            criado_por=cliente,
        )

        agendamento.save()
        usuario.save()
        messages.success(request, f'Agendamento de horário realizado com sucesso!')

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


def alterar_horario_atendimento(duracao_servico, horario_atendimento):
    # Converte horario_disponivel para datetime.datetime
    horario_datetime = datetime.combine(datetime.today(), horario_atendimento.horario_disponivel)

    # Adiciona a duracao
    horario_datetime += timedelta(minutes=duracao_servico.minute, seconds=duracao_servico.second)

    # Converte de volta para datetime.time
    novo_horario_disponivel = horario_datetime.time()

    return novo_horario_disponivel


def alterar_horario_atendimento_e_adicionar_intervalo(duracao_servico, horario_selecionado, horario_atendimento):
    # Converte horario_disponivel para datetime.datetime
    horario_datetime = datetime.combine(datetime.today(), horario_atendimento.horario_disponivel)

    # Adiciona a duração ao horário selecionado para agendamento
    horario_datetime += timedelta(minutes=duracao_servico.minute, seconds=duracao_servico.second)

    # Converte de volta para datetime.time
    novo_horario_disponivel = horario_datetime.time()

    # Adiciona 30 minutos apenas aos horários após o horário selecionado para agendamento
    if horario_atendimento.horario_disponivel >= horario_selecionado:
        novo_horario_disponivel += timedelta(minutes=30)

    return novo_horario_disponivel


def cancelar_agendamento(request, agenda_id):
    agendamento = Agendamento.objects.get(id=agenda_id)
    if agendamento.status_agendamento == 'AG':
        agendamento.status_agendamento = 'CA'
        agendamento.save()
        if agendamento.status_agendamento == 'CA':
            messages.error(request, f'Agendamento cancelado com sucesso')
            return redirect('listar_agendamentos_cliente')

def concluir_agendamento(request, agendamento_id):
    agendamentos = Agendamento.objects.all()
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    usuario = agendamento.cliente

    if agendamento.status_agendamento == 'AG':
        agendamento.status_agendamento = 'CO'
        agendamento.save()
        usuario.save()

        agendamentos_cliente = Agendamento.objects.filter(cliente=agendamento.cliente, status_agendamento='CO')
        quantidade = agendamentos_cliente.count()
        if usuario.fidelidade is not None:
            if quantidade % usuario.fidelidade.requisito == 0:
                usuario.desconto = usuario.fidelidade.desconto

                usuario.save()

    if agendamento.status_agendamento == 'CO':
        messages.success(request, f'Agendamento concluido concluido com sucesso!')
        redirect('listar_agendamentos')

    context = {
        'agendamentos': agendamentos
    }

    return render(request, "assets/static/crud_agenda/lista_agendamentos.html", context)

# def get_horarios_disponiveis(request):
#     if request.is_ajax() and request.method == 'GET':
#         dia_id = request.GET.get('dia_id')
#         horarios = Horarios.objects.filter(disponibilidade__dia__id=dia_id).values_list('horario_disponivel', flat=True)
#         horarios_disponiveis = list(horarios)
#
#         return JsonResponse({'horarios': horarios_disponiveis}, safe=False)
#     else:
#         return JsonResponse({'error': 'Invalid request'})