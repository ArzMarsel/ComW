from django.contrib import admin
from .models import Grade, Connect, Assignment, Course, Lecture

admin.site.register(Lecture)
admin.site.register(Grade)
admin.site.register(Connect)
admin.site.register(Assignment)
admin.site.register(Course)

