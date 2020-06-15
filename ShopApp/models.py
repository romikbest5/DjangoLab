from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    name = models.CharField('название товара', max_length=200)
    description = models.TextField('описание товара')
    price = models.FloatField('цена товара')

    def __str__(self):
        return self.name

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('текст комента')
    added = models.DateField('дата добавления', default=timezone.now)
    mark = models.IntegerField('оценка')

    def __str__(self):
        return self.text