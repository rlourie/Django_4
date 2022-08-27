from django.contrib import admin

from .models import Student, Teacher


class RelatinsInLine(admin.TabularInline):
    model = Student.teacher.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        RelatinsInLine
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        RelatinsInLine
    ]
