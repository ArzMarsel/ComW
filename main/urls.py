from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('unauthenticated/', views.unauthenticated, name='unauthenticated'),
    path('register/', views.register, name='register'),
    path('', views.main, name='main'),
]