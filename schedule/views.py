import datetime
from django.shortcuts import render
from .models import DaySchedule, Lesson

def schedule_view(request):
    today_idx = datetime.date.today().weekday()
    tomorrow_idx = (today_idx + 1) % 6  # wrap around Mon-Sat

    today_schedule = DaySchedule.objects.filter(weekday=today_idx).first()
    tomorrow_schedule = DaySchedule.objects.filter(weekday=tomorrow_idx).first()

    context = {
        "today": today_schedule,
        "tomorrow": tomorrow_schedule,
    }
    return render(request, "schedule.html", context)
