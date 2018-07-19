from django.shortcuts import render
from django.shortcuts import redirect
from . import forms
from . import models
# Create your views here.

def login(request):
    if request.method == 'POST':
        login_form = forms.User(request.POST)
        if login_form.is_valid():
            name = login_form.cleaned_data['userId']
            pwd = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=name)
                if user.password == pwd:
                    return render(request, 'login/home.html')
                else:
                    print("pwd is wrong")
            except:
                print("用户不存在")
        return render(request, 'login/login.html')
    login_form = forms.User()
    return render(request, 'login/login.html', locals())


def home(request):
    home_form =forms.Host(request.GET)
    info = models.Host.objects.all()
    print(info)

    return render(request, 'login/home.html')