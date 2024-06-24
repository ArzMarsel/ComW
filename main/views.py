from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import Error
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm, AssignmentForm, LectureForm, GradeForm, AnswerForm
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
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def start(request):
    return render(request, 'lectures/start.html')


@login_required(login_url='unauthenticated')
def main(request):
    prof = Profile.objects.filter(user=request.user)
    courses = Course.objects.all().prefetch_related('courseimage_set')
    course_with_images = [
        (course, course.courseimage_set.all()[0].image.url if course.courseimage_set.exists() else None)
        for course in courses
    ]
    return render(request, 'lectures/main.html', {'course_with_images': course_with_images, 'prof': prof})


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
    prof = Profile.objects.filter(user=request.user)
    courses = Course.objects.filter(teachers=request.user).prefetch_related('courseimage_set')
    course_with_images = [
        (course, course.courseimage_set.all()[0].image.url if course.courseimage_set.exists() else None)
        for course in courses
    ]
    return render(request, 'lectures/my courses.html', {'course_with_images': course_with_images, 'prof': prof})


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
def assignment_list(request, pk):
    course = get_object_or_404(Course, pk=pk)
    assign = Assignment.objects.filter(course=course)
    return render(request, 'lectures/assignments.html', {'assign': assign, 'course': course})


@login_required(login_url="unauthenticated")
def connect_to_corsina(request):
    cors = Connect.objects.filter(user=request.user)
    return render(request, 'lectures/corsina.html', {'cors': cors})


@login_required(login_url="unauthenticated")
def add_assign(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.course = course
            assignment.save()
            return redirect('my courses')
    else:
        form = AssignmentForm()

    return render(request, 'lectures/add assign.html', {'form': form})


@login_required(login_url="unauthenticated")
def add_grade(request, pk):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        form.course = get_object_or_404(Course, pk=pk)
        if form.is_valid():
            form.save()
    else:
        form = GradeForm()
    return render(request, 'lectures/add grade.html', {'form': form})


@login_required(login_url="unauthenticated")
def add_answer(request, pk1):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.student = get_object_or_404(User, user=request.user)
        form.assignment = get_object_or_404(Assignment, pk=pk1)
        if form.is_valid():
            form.save()
    else:
        form = AnswerForm()
    return render(request, 'lectures/add answer.html', {'form': form})


@login_required(login_url="unauthenticated")
def add_lecture(request, pk):
    if request.method == 'POST':
        form = LectureForm(request.POST)
        form.course = get_object_or_404(Course, pk=pk)
        if form.is_valid():
            form.save()
    else:
        form = LectureForm()
    return render(request, 'lectures/add lecture.html', {'form': form})


@login_required(login_url="unauthenticated")
def lectures_list(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lectures = Lecture.objects.filter(course=course)
    return render(request, 'lectures/lectures.html', {'course': course, 'lectures': lectures})


@login_required(login_url="unauthenticated")
def answers_list(request, pk):
    course = get_object_or_404(Course, pk=pk)
    answers = Answer.objects.filter(course=course)
    return render(request, 'lectures/answers.html', {'course': course, 'answers': answers})
