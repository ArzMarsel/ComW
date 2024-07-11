from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField('Название:', max_length=20)
    description = models.TextField('Описание:')
    start_date = models.DateField('Дата начала:')
    end_date = models.DateField("Дата окончания:")
    teachers = models.ForeignKey(User, related_name='teachers', on_delete=models.CASCADE)


class CourseImage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', verbose_name='Изображения:')


class Lecture(models.Model):
    lecture_video = models.FileField(upload_to='lectures/', max_length=5*1024*1024)
    title = models.CharField(max_length=100, verbose_name='Title:')
    course = models.ForeignKey(Course, verbose_name='Course:', on_delete=models.CASCADE)


class Assignment(models.Model):
    title = models.CharField('Название задания:', max_length=255)
    description = models.TextField('Описание задания:')
    due_date = models.DateField('Срок сдачи:')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='answer')
    file = models.FileField(upload_to='answers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of create:')


class Grade(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField('Оценка', null=True, blank=True)
    comment = models.TextField('Комментарии', null=True, blank=True)
    date1 = models.DateField(verbose_name='Date of grade:', auto_now_add=True)


class Connect(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course:', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user:')


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = (
        ('user', '-'),
        ('teacher', 'Учитель'),
        ('student', 'Ученик')
    )
    user_status = models.CharField(choices=status_choices, max_length=20)


class Zaiavka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mark = models.BooleanField()
