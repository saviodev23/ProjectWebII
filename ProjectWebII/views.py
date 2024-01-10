from django.contrib.auth.models import Group
from django.shortcuts import render
from ProjectWebII.utils import create_groups
from agenda.models import Servico


def home(request):
    create_groups()
    servicos = Servico.objects.all()
    context = {
        'servicos': servicos
    }
    return render(request, 'assets/static/index.html', context)

def filtrar_usuarios_acesso_administrativo(request):
    profissional_group = Group.objects.get(name='Profissional')
    profissionais = profissional_group.user_set.all()
    # grupos = request.user.groups.filter(name__in=['Profissional', 'Administrador']).exists()
    return render(request, 'assets/static/index.html', {'grupos': profissionais})