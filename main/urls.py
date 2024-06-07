from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('unauthenticated/', views.unauthenticated, name='unauthenticated'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.main, name='main'),
    path('about us/', views.about_us, name='about us'),
    # path('courses/<int:course_pk>/assignments/', views.assignment_list, name='assignment_list'),
    # path('assignments/<int:assignment_pk>/grade/', views.grade_assignment, name='grade_assignment'),
    # path('courses/<int:course_id>/add/', views.add_assignment_to_course, name='add_assignment_to_course'),
    path('courses/<int:pk>/', views.course_detail, name='detail'),
    path('courses1/<int:pk>/', views.course_detail1, name='detail1'),
    path('courses2/<int:pk>/', views.course_detail2, name='detail2'),
    path('my_courses_t/', views.my_courses, name='my courses'),
    path('my_courses_s/', views.my_courses2, name='my courses2'),
]