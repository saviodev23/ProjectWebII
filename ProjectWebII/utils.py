from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from agenda.models import Agendamento, Fidelidade, Servico
from accounts.models import Usuario
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



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


    


#@group_required(['Cliente'], "/accounts/login/")
#def mostrar_pontos(request, user_id):
    #usuario = get_object_or_404(Usuario, pk=user_id)
    #agendamentos = Agendamento.objects.filter(cliente=request.user).order_by('-dia', 'horario')
    #quantidade = agendamentos.count
    #cupon = usuario.cupon

    #context = {
        #'quantidade':quantidade,
        #'cupon':cupon,
        #'agendamentos':agendamentos

    #}
    #return render(request, 'assets/static/crud_Fidelidade/mostrar_pontos', context)
@group_required(['Cliente'], "/accounts/login/")
def resgatar_fidelidade(request, fidelidade_id):
    usuario = request.user
    fidelidade = get_object_or_404(Fidelidade, pk=fidelidade_id)
    usuario.fidelidade = fidelidade

    usuario.save()

    servicos = Servico.objects.all()
    fidelidades = Fidelidade.objects.all()
    context = {
        'servicos': servicos,
        'fidelidades':fidelidades
    }

    return render(request, 'assets/static/index.html', context)

@group_required(['Cliente'], "/accounts/login/")
def mostrar_pontos(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    agendamentos = Agendamento.objects.filter(cliente=request.user,status_agendamento='CO').order_by('-dia', 'horario')
    fidelidade = usuario.fidelidade
    quantidade = agendamentos.count()
    valor = quantidade % fidelidade.requisito
    desconto = usuario.desconto
    falta = fidelidade.requisito - valor

    context = {
        'fidelidade':fidelidade,
        'desconto':desconto,
        'falta':falta,
        

    }
    return render(request, 'assets/static/crud_Fidelidade/mostrar_pontos', context)


@group_required(['Cliente'], "/accounts/login/")
def remover_fidelidade_cliente(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    usuario.fidelidade = None
    usuario.save()


    return redirect('mostrar_pontos', user_id=user_id)