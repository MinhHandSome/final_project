from django import template
from django.core.checks import messages
from django.forms.forms import Form
from django.http import response
from django.views.generic import edit
from myapp import models
from django.shortcuts import redirect, render, get_object_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm,LoginForm
from myapp import forms
from django.contrib.auth import views as auth_views
def register_user(request):
    form = RegisterForm
    message = ""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save_user()
            return redirect('index')
    return render(
        request=request,
        template_name='user/register.html',
        context={
            'form':form,
            "message":message
        }
    )
def login_user(request):
    form = LoginForm
    message=""
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user :
                login(request,user)
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                return redirect('index')
            else :
                message = "Thông tin sai. Vui lòng nhập lại"
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return render(
        request=request,
        template_name='user/login.html',
        context={
            'form':form,
            'message':message
        }
    )