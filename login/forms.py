from . import models
from django import forms
class User(forms.Form):
    userId = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=216)