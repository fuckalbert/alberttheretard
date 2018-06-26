# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mybooks.models import Book, Boo, Comment

admin.site.register(Book)
admin.site.register(Boo)
admin.site.register(Comment)
