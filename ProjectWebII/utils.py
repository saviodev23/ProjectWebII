from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied

from horario.models import Parametro
from datetime import datetime, timedelta


def group_required(groups, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a group permission,
    redirecting to the log-in page if necessary.
    If the raise_exception parameter is given, the PermissionDenied exception
    is raised.
    """

    def check_perms(user):
        if isinstance(groups, list):
            group_names = groups
        else:
            group_names = [groups]

        # First check if the user has the permission (even anon users)
        if user.groups.filter(name__in=group_names).exists():
            return True

        # In case the 403 handler should be called, raise the exception
        if raise_exception:
            raise PermissionDenied

        # As the last resort, show the login form
        return False

    return user_passes_test(check_perms, login_url=login_url)


#executa apenas uma vez para criar os grupos quando abre a página home
def create_groups():
    if not Group.objects.exists():
        groupAdmin = Group(name='Administrador')
        groupAdmin.save()

        groupAdmin = Group(name='Cliente')
        groupAdmin.save()

        groupAdmin = Group(name='Profissional')
        groupAdmin.save()



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



def alterar_horario_atendimento(duracao_servico, horario_atendimento):
    # Converte horario_disponivel para datetime.datetime
    horario_datetime = datetime.combine(datetime.today(), horario_atendimento.horario_disponivel)

    # Adiciona a duracao
    horario_datetime += timedelta(minutes=duracao_servico.minute, seconds=duracao_servico.second)

    # Converte de volta para datetime.time
    novo_horario_disponivel = horario_datetime.time()

    return novo_horario_disponivel




