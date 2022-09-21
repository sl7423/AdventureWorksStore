from django import forms
from .models import Account
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control-email'})
        self.fields['password'].widget.attrs.update({'class':'form-control-password'})