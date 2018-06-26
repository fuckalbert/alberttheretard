# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

FANTASY = 0
ACTION = 1
ADVENTURE = 2
STRATEGY = 3
HORROR = 4
RPG = 5
SPORT = 6
SHOOTER = 7


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(User, verbose_name='Developer')

    class Meta:
        abstract = True


class Book(Base):

    class Meta:
        ordering = ('name', 'created')
        verbose_name = u'Книжка'
        verbose_name_plural = u'Книжки'

    GENRES = (
        (FANTASY, 'fantasy'),
        (ACTION, 'action'),
        (ADVENTURE, 'adventure'),
        (STRATEGY, 'strategy'),
        (HORROR, 'horror'),
        (RPG, 'rpg'),
        (SPORT, 'sport'),
        (SHOOTER, 'shooter'),
    )
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(verbose_name=u'About game')
    year = models.PositiveSmallIntegerField()
    img = models.ImageField(upload_to='books/', null=True, blank=True)
    genre = models.SmallIntegerField(choices=GENRES, default=0)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Boo(Base):
    name = models.CharField(max_length=200, db_index=True)

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    text = models.TextField()
    game = models.ForeignKey(Book)




