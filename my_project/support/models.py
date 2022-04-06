from django.contrib.auth.models import User
from django.db import models


# Create your models here

class Ticket(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема')
    content = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    stat = models.ForeignKey('Status', on_delete=models.PROTECT, null=True, verbose_name='Статус')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'


class Status(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class CommentTicket(models.Model):
    '''Модель комментариев'''
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name='Родитель')
    text = models.TextField("Текст комментария", max_length=500)
    created = models.DateTimeField("Добавлен", auto_now_add=True)
    ticket = models.ForeignKey(Ticket, verbose_name='Тикет', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
