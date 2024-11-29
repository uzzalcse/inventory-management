from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Choice, Student, Teacher

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Student)
admin.site.register(Teacher)