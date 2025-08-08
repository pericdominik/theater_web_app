from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Dobrodošli natrag!")
            return redirect('index') 
        else:
            messages.error(request, "Neispravni podaci (email ili lozinka).")

    return render(request, 'kazaliste/login.html')

def user_logout(request):
    logout(request)
    messages.info(request, "Uspješno ste se odjavili.")
    return redirect('index')


@login_required(login_url='login')
def my_account(request):
    return render(request, 'kazaliste/my_account.html')