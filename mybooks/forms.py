from django import forms

from books.forms import BootstrapFormMixin
from mybooks.models import Book, Comment


class BookAddForm(forms.ModelForm, BootstrapFormMixin):

    class Meta:
        model = Book
        exclude = ('approved',)

    def __init__(self, *args, **kwargs):
        super(BookAddForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)
        self.fields['description'].widget.attrs['rows'] = 5


class CommentForm(forms.ModelForm, BootstrapFormMixin):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)

    class Meta:
        model = Comment
        exclude = ('author', 'game')
