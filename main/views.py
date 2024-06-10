from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LoginForm, UserCreation
from .models import Course, Lecture, Answer, Grade, Assignment, Connect


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
    user = request.user
    course = Course.objects.all()
    return render(request, 'lectures/main.html', {'course': course, 'user': user})


@login_required(login_url='unauthenticated')
def about_us(request):
    return render(request, template_name='lectures/about us.html')


@login_required(login_url='unauthenticated')
def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    lecture = Lecture.objects.filter(course=course)
    return render(request, 'lectures/detail.html', {'course': course, 'lecture': lecture})


@login_required(login_url='unauthenticated')
def course_detail1(request, pk):
    course = Course.objects.get(id=pk)
    lecture = Lecture.objects.filter(course=course)
    return render(request, 'lectures/detail1.html', {'course': course, 'lecture': lecture})


@login_required(login_url='unauthenticated')
def course_detail2(request, pk):
    course = Course.objects.get(id=pk)
    lecture = Lecture.objects.filter(course=course)
    return render(request, 'lectures/detai2l.html', {'course': course, 'lecture': lecture})


@login_required(login_url='unauthenticated')
def my_courses(request):
    user = request.user
    course = Course.objects.filter(teachers=user)
    return render(request, 'lectures/my courses.html', {'course': course, 'user': user})


@login_required(login_url='unauthenticated')
def my_courses2(request):
    user = request.user
    connect = Connect.objects.filter(user=user)
    return render(request, 'lectures/my courses2.html', {'connect': connect, 'user': user})


@login_required(login_url='unauthenticated')
def assignments(request):
    course = get_object_or_404(Course, )
    assign = Assignment.objects.filter(course=course)
    return render(request, 'lectures/assignments.html', {'assign': assign})


@login_required(login_url='unauthenticated')
def my_courses(request):
    course = get_object_or_404(Course, )
    assign = Assignment.objects.filter(course=course)
    return render(request, 'lectures/.html', {'assign': assign})


