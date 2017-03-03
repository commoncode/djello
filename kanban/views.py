from django.shortcuts import render

from .models import Board


def index(request):
    return render(request, template_name='kanban/base.html', context={
        'boards': Board.objects.all(),
    })
