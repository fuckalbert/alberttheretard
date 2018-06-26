# coding=utf-8
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.extras import SelectDateWidget


class BootstrapFormMixin:
    def __init__(self):
        for field_name, field in self.fields.iteritems():
            if not isinstance(field.widget, (forms.TextInput, SelectDateWidget, forms.NumberInput, forms.URLInput,
                                             forms.Textarea, forms.Select, forms.FileInput)):
                continue
            attrs = field.widget.attrs
            if 'class' in attrs:
                if attrs['class']:
                    attrs['class'] += ' '
            else:
                attrs['class'] = ''
            attrs['class'] += 'form-control'


class LoginForm(AuthenticationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)

    def clean(self):
        has_error = False
        try:
            super(LoginForm, self).clean()
        except forms.ValidationError:
            has_error = True
        if has_error or self.errors or self.user_cache:
            self._errors.clear()
            raise forms.ValidationError(u'Неправильно введений email або пароль')