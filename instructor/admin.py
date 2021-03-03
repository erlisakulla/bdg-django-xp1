from django.contrib import admin

# Register your models here.

from .models import Instructor
from student.models import Student

admin.site.register(Instructor)
admin.site.register(Student)