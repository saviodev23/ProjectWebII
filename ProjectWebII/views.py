from django.shortcuts import render

from ProjectWebII.utils import create_groups


def home(request):
    create_groups()
    return render(request, 'assets/static/index.html')