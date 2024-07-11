from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import Error
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm, AssignmentForm, LectureForm, GradeForm, AnswerForm
from .models import Course, Lecture, Answer, Grade, Assignment, Connect, Profile, Zaiavka


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
    prof = get_object_or_404(Profile, user=request.user)
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
    return render(request, 'lectures/detail2.html', {'course': course, 'lecture': lecture})


@login_required(login_url='unauthenticated')
def my_courses(request):
    prof = get_object_or_404(Profile, user=request.user)
    courses = Course.objects.filter(teachers=request.user).prefetch_related('courseimage_set')
    course_with_images = [
        (course, course.courseimage_set.all()[0].image.url if course.courseimage_set.exists() else None)
        for course in courses
    ]
    return render(request, 'lectures/my courses.html', {'course_with_images': course_with_images, 'prof': prof})


@login_required(login_url='unauthenticated')
def my_courses2(request):
    prof = Profile.objects.filter(user=request.user)
    courses = Connect.objects.filter(user=request.user).prefetch_related('course__courseimage_set')
    course_with_images = [
        (i, i.course, i.course.courseimage_set.all()[0].image.url if i.course.courseimage_set.exists() else None)
        for i in courses
    ]
    return render(request, 'lectures/my courses2.html', {'course_with_images': course_with_images, 'prof': prof})


@login_required(login_url='unauthenticated')
def assignment_list(request, pk):
    prof = get_object_or_404(Profile, user=request.user)
    course = get_object_or_404(Course, pk=pk)
    assign = Assignment.objects.filter(course=course)
    return render(request, 'lectures/assign.html', {'assign': assign, 'course': course, 'prof': prof})


@login_required(login_url='unauthenticated')
def assignment_list2(request, pk):
    prof = get_object_or_404(Profile, user=request.user)
    course = get_object_or_404(Course, pk=pk)
    assign = Assignment.objects.filter(course=course)
    return render(request, 'lectures/assign2.html', {'assign': assign, 'course': course, 'prof': prof})


@login_required(login_url='unauthenticated')
def answers_list(request, pk):
    prof = get_object_or_404(Profile, user=request.user)
    assign = get_object_or_404(Assignment, pk=pk)
    answer = Answer.objects.filter(assignment=assign)
    return render(request, 'lectures/answers.html', {'answer': answer, 'assign': assign, 'prof': prof})


@login_required(login_url="unauthenticated")
def add_assign(request, pk):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.course = get_object_or_404(Course, pk=pk)
            assignment.save()
            return redirect('my courses')
    else:
        form = AssignmentForm()
        print(form.errors)
    return render(request, 'lectures/add assign.html', {'form': form})


@login_required(login_url="unauthenticated")
def add_answer(request, pk):
    if request.method == 'POST':

        form = AnswerForm(request.POST, request.FILES)

        print(form.errors)
        form.student = get_object_or_404(User, pk=request.user.id)
        form.assignment = get_object_or_404(Assignment, pk=pk)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.student = request.user
            answer.assignment = get_object_or_404(Assignment, pk=pk)
            answer.save()
            form.save()
            return redirect('main')
    else:

        form = AnswerForm()
        print(form.errors)
    return render(request, 'lectures/add answer.html', {'form': form})


@login_required(login_url="unauthenticated")
def add_lecture(request, pk):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        form.course = get_object_or_404(Course, pk=pk)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.course = get_object_or_404(Course, pk=pk)
            lecture.save()
            return redirect('my courses')
        else:
            print(form.errors)
    else:
        form = LectureForm()

    return render(request, 'lectures/add lecture.html', {'form': form})


@login_required(login_url="unauthenticated")
def lectures_list(request, pk):
    prof = get_object_or_404(Profile, user=request.user)
    course = get_object_or_404(Course, pk=pk)
    lectures = Lecture.objects.filter(course=course)
    return render(request, 'lectures/lectures.html', {'course': course, 'lectures': lectures, 'prof': prof})


@login_required(login_url="unauthenticated")
def zaiavka(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Zaiavka.objects.create(user=request.user, course=course, mark=True)
    return redirect("main")


@login_required(login_url="unauthenticated")
def zaiavka_list(request, pk):
    prof = get_object_or_404(Profile, user=request.user)
    course = get_object_or_404(Course, pk=pk)
    zaiavka = Zaiavka.objects.filter(course=course, mark=True)
    return render(request, 'lectures/zaiavka.html', {"zaiavka" : zaiavka, 'prof': prof})


@login_required(login_url="unauthenticated")
def add_connect(request, pk):
    zaiavka = get_object_or_404(Zaiavka, pk=pk)
    Connect.objects.create(course=zaiavka.course, user=zaiavka.user)
    zaiavka.mark = False
    zaiavka.save()
    return redirect("my courses")


@login_required(login_url="unauthenticated")
def add_grade(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = answer.student
            grade.answer = answer
            grade.save()
            return redirect('my courses')
        else:
            print(form.errors)
    else:
        form = GradeForm()
    return render(request, 'lectures/add grade.html', {'form': form})
