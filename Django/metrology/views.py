from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Metrology
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Успех!")
            return redirect("login")
        else:
            messages.error(request, "Ошибка!")
    else:
        form = UserRegisterForm()
    return render(request, 'metrology/register.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, 'metrology/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    metrology = Metrology.objects.all()
    template_index = 'metrology/index.html'
    context = {
        'metrology': metrology,
        'title': 'Автосервис - Нитрон',
        'text': 'Услуги',
    }
    return render(request, template_index, context)

class CreateMetr(CreateView):
    form_class = NewsForm
    template_name = 'metrology/add_cont.html'
    success_url = '/'