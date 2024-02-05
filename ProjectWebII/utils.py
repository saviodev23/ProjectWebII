from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied

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

        groupAdmin = Group(name='Secretaria')
        groupAdmin.save()








