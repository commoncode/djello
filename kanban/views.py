import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Board, Card, Column


@ensure_csrf_cookie
def index(request):
    return render(request, template_name='kanban/base.html', context={
        'boards': Board.objects.all(),
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
