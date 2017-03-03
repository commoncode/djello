from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Column(models.Model):
    board = models.ForeignKey('Board', related_name='columns')
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{} - {}'.format(self.board.name, self.title)


class Card(models.Model):
    column = models.ForeignKey('Column', related_name='cards')
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{} - {} - {}'.format(self.column.board.name, self.column.title, self.title)
