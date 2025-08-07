from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Account
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'kazaliste/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                form.add_error('email', "Email adresa je već iskorištena.")
                return render(request, 'kazaliste/register.html', {'form': form})

            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )

            Account.objects.create(
                user=user,
                phone=form.cleaned_data['phone']
            )

            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'kazaliste/register.html', {'form': form})