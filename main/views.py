from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, UserCreation, ProfileForm
from .models import Course, Lecture, Answer, Grade, Assignment, Connect, Profile


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
        form1 = ProfileForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user1 = form1.save()
            return redirect('login')
    else:
        form = UserCreation()
        form1 = ProfileForm()
    return render(request, 'accounts/register.html', {'form1': form1, 'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def start(request):
    return render(request, 'lectures/start.html')


@login_required(login_url='unauthenticated')
def main(request):
    user = Profile.objects.filter(user=request.user)
    courses = Course.objects.all().prefetch_related('courseimage_set')
    course_with_images = [
        (course, course.courseimage_set.all()[0].image.url if course.courseimage_set.exists() else None)
        for course in courses
    ]
    return render(request, 'lectures/main.html', {'course_with_images': course_with_images, 'user': user})


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
    user = Profile.objects.filter(user=request.user)
    courses = Course.objects.filter(teachers=user).prefetch_related('courseimage_set')
    course_with_images = [
        (course, course.courseimage_set.all()[0].image.url if course.courseimage_set.exists() else None)
        for course in courses
    ]
    return render(request, 'lectures/my courses.html', {'course_with_images': course_with_images, 'user': user})


@login_required(login_url='unauthenticated')
def my_courses2(request):
    user = Profile.objects.filter(user=request.user)
    course1 = Connect.objects.filter(user=user)
    courses = course1.course.prefetch_related('courseimage_set')
    course_with_images = [
        (course, course.courseimage_set.all()[0].image.url if course.courseimage_set.exists() else None)
        for course in courses
    ]
    return render(request, 'lectures/my courses.html', {'course_with_images': course_with_images, 'user': user})


@login_required(login_url='unauthenticated')
def assignments(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    assign = Assignment.objects.filter(course=course)
    return render(request, 'lectures/assignments.html', {'assign': assign})


@login_required(login_url="unauthenticated")
def connect_to_corsina(request):
    cors = Connect.objects.filter(user=request.user)
    return render(request, 'restaurant/corsina.html', {'cors': cors})

