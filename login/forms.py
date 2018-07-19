from . import models
from django import forms
class User(forms.Form):
    userId = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=216)


class Host(forms.Form):
    ip = forms.GenericIPAddressField()
    user = forms.CharField(label="账号", max_length=128)
    password = forms.CharField(label="密码", max_length=216)
    tag = forms.CharField(label="备注", max_length=1024)
    item = forms.CharField(label="项目", max_length=1024)