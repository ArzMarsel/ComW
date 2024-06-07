from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm, UserCreation
from .models import Course, Lecture, Answer, Grade, Assignment


def unauthenticated(request):
    return render(request, 'accounts/unauthenticated.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password1'])
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                form.add_error(None, 'Ошибка в имени или пароле!')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreation()
    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def main(request):
    username = request.user.username
    course = Course.objects.all()
    return render(request, 'lectures/main.html', {'courses': course, 'username': username})


@login_required(login_url='unauthenticated')
def about_us(request):
    return render(request, template_name='lectures/about us.html')


@login_required(login_url='unauthenticated')
def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'lectures/detail.html', {'course': course})


