from django.contrib import admin

from .models import Board, Card, Column

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Card)
