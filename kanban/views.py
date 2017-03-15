import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Board, Card, Column


@ensure_csrf_cookie
def index(request):
    return render(request, template_name='kanban/base.html', context={
        'boards': Board.objects.all(),
    })


def new_card(request):
    column_id = int(request.POST.get('column_id'))
    title = request.POST.get('title')
    assert title and column_id
    Card.objects.create(title=title, column_id=column_id)
    return redirect('/')


def view_card(request, card_id, card_slug):
    return render(request, template_name='kanban/view.html', context={
        'boards': Board.objects.all(),
        'current_card': Card.objects.get(id=card_id),
    })


def drop(request):
    payload = json.loads(request.body)
    card_id = int(payload.get('card_id'))
    column_id = int(payload.get('column_id'))
    assert card_id and column_id
    card = Card.objects.get(id=card_id)
    card.column = Column.objects.get(id=column_id)
    card.save()
    return HttpResponse()
