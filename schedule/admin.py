from django.contrib import admin
from .models import Subject, Lesson, DaySchedule

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 7
    ordering = ("period",)
    fields = ("period", "subject")


@admin.register(DaySchedule)
class DayScheduleAdmin(admin.ModelAdmin):
    list_display = ("weekday",)
    inlines = [LessonInline]
    ordering = ("weekday",)
