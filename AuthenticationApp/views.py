from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from .forms import UserRegisterForm, UserLoginForm


def login(request):
    patterns = 'Authentication/Login.html'
    context = {
        'form': None
    }

    if request.user.is_authenticated:
        url = request.GET.get('next') or reverse('main')
        return redirect(url)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)

                url = request.GET.get('next') or reverse('main')
                return redirect(url)
            else:
                form.add_error('password', 'Invalid credentials!')
        context['form'] = form
    else:
        context['form'] = UserLoginForm()

    return render(request, patterns, context)


def logout(request):
    patterns = 'Authentication/Login.html'
    context = {

    }

    auth.logout(request)
    url = request.GET.get('next') or reverse('main')
    return redirect(url)


def register(request):
    patterns = 'Authentication/Register.html'
    context = {
        'form': None
    }

    if request.user.is_authenticated:
        url = request.GET.get('next') or reverse('main')
        return redirect(url)

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            password2 = form.cleaned_data.get('repeat_password', None)
            if password == password2:
                users_in_base = auth.models.User.objects.filter(username=username).first()
                if users_in_base is None:
                    new_user = auth.models.User.objects.create_user(username, '', password)
                    auth.login(request, new_user)

                    url = request.GET.get('next') or reverse('main')
                    return redirect(url)
                else:
                    form.add_error('username', 'User already existed')
            else:
                form.add_error('repeat_password', 'Passwords did not match')
        context['form'] = form
    else:
        context['form'] = UserRegisterForm()

    return render(request, patterns, context)