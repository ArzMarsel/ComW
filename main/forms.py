from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from .models import Profile,Assignment


class AssignmentForm(forms.ModelForm):
    title = forms.CharField(
        label='Название задания:',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'})
    )
    description = forms.CharField(
        label='Описание задания:',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'})
    )
    due_date = forms.DateField(
        label='Срок сдачи:',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date']


class GradeForm(forms.ModelForm):
    grade = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Grade'
            }
        )
    )
    comment = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Comment'
            }
        )
    )

    class Meta:
        model = models.Grade
        fields = '__all__'


class SignUpForm(UserCreationForm):
    user_status = forms.ChoiceField(choices=Profile.status_choices, required=True, label="Статус")
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password 1'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password 2'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'user_status')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(user=user, user_status=self.cleaned_data['user_status'])
        return user


class ProfileForm(forms.Form):
    # captcha = ReCaptchaField()
    user = UserCreationForm()
    status_choices = (
        ('user', '-'),
        ('teacher', 'Учитель'),
        ('student', 'Ученик')
    )
    user_status = forms.ChoiceField(choices=status_choices)

    class Meta:
        model = Profile
        fields = ['user', 'user_status']


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password1']


class LectureForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }
        )
    )
    lecture_video = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'File'
            }
        )
    )

    class Meta:
        model = models.Lecture
        exclude = ['course']


class AnswerForm(forms.ModelForm):
    answer = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Answer'
            }
        )
    )
    content = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Content'
            }
        )
    )

    class Meta:
        model = models.Answer
        fields = '__all__'
