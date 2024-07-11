from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('unauthenticated/', views.unauthenticated, name='unauthenticated'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.main, name='main'),
    path('my_courses_t/', views.my_courses, name='my courses'),
    path('my_courses_s/', views.my_courses2, name='my courses2'),
    path('', views.start, name='start'),
    path('about us/', views.about_us, name='about us'),
    path('courses1/<int:pk>/lectures/', views.lectures_list, name='lectures'),
    path('courses1/<int:pk>/assign/', views.assignment_list, name='assign'),
    path('courses2/<int:pk>/assign/', views.assignment_list2, name='assign2'),
    path('courses2/<int:pk>/answers/', views.answers_list, name='answer'),
    path('courses/<int:pk>/', views.course_detail, name='detail'),
    path('courses1/<int:pk>/', views.course_detail1, name='detail1'),
    path('courses2/<int:pk>/', views.course_detail2, name='detail2'),
    path('courses1/<int:pk>/assign/add/', views.add_assign, name='add assign'),
    path('courses1/<int:pk>/lectures/add/', views.add_lecture, name='add lecture'),
    path('courses2/<int:pk>/answers/add/', views.add_answer, name='add answer'),
    path('courses/<int:pk>/zaiavka', views.zaiavka, name='zaiavka'),
    path('courses2/<int:pk>/zaiavka_list/', views.zaiavka_list, name='zaiavka_list'),
    path('courses1/<int:pk>/connect/add/', views.add_connect, name='add connect'),
    path('courses2/<int:pk>/answers/add/', views.add_grade, name='add grade')
]