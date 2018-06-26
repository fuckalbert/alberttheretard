# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView


from mybooks.forms import BookAddForm, CommentForm
from mybooks.models import Book, Comment
from books.forms import LoginForm


def main_page(request):
    search = request.GET.get('search')
    if search:
        books = Book.objects.filter(name__icontains=search)
    else:
        books = Book.objects.filter(approved=True)
    return render(request, 'main.html', {'games': books, 'search': search if search else ''})


def add_book_page(request):
    form = BookAddForm((request.POST or None), (request.FILES or None))
    added = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            added = True
    return render(request, 'add_book_form.html', {'form': form, 'added': added})


def book_page(request, book_id):
    game = get_object_or_404(Book, id=book_id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.game = Book.objects.get(pk=book_id)
            obj.save()
            return redirect(request.path)
    return render(request, 'single_book.html', {'game': game, 'form': form})

# def login_view(request):
#     if request.user.is_authenticated():
#         return redirect('main_page')
#     return login(request, 'login.html', authenticated_form=LoginForm)

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'
