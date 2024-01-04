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