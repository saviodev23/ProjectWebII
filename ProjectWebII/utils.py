from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from agenda.models import Agendamento, Fidelidade
from accounts.models import Usuario
from django.shortcuts import render, get_object_or_404


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


    
def resgatar_cupon(fidelidade_id, usuario_id):
    
    fidelidade = get_object_or_404(Fidelidade, id=fidelidade_id)
    usuario =  get_object_or_404(Usuario, id=usuario_id)
    
    cupon = fidelidade.cupon

    cupon = cupon-1
    usuario.desconto = 1

 
def mostrar_pontos(request, agendamento_id,cupon_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    fidelidade = get_object_or_404(Fidelidade, id=cupon_id)

    context = {
        'agendamento':agendamento,
        'fidelidade':fidelidade
    }
    return render(request, 'assets/static/crud_fidelidade/mostrar_pontos', context)