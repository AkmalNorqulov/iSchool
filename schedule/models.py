from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    WEEKDAYS = [
        (0, "Dushanba"),
        (1, "Seshanba"),
        (2, "Chorshanba"),
        (3, "Payshanba"),
        (4, "Juma"),
        (5, "Shanba"),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.ForeignKey("DaySchedule", on_delete=models.CASCADE, related_name="lessons")
    period = models.PositiveIntegerField()

    class Meta:
        ordering = ["period"]

    def __str__(self):
        return f"{self.day} - {self.subject}"


class DaySchedule(models.Model):
    weekday = models.IntegerField(choices=Lesson.WEEKDAYS, unique=True)

    class Meta:
        ordering = ["weekday"]

    def __str__(self):
        return dict(Lesson.WEEKDAYS)[self.weekday]
