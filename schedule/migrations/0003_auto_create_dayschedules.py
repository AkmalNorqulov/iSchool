from django.db import migrations

def create_days(apps, schema_editor):
    DaySchedule = apps.get_model("schedule", "DaySchedule")
    weekdays = [
        (0, "Dushanba"),
        (1, "Seshanba"),
        (2, "Chorshanba"),
        (3, "Payshanba"),
        (4, "Juma"),
        (5, "Shanba"),
    ]
    for wd, _ in weekdays:
        DaySchedule.objects.get_or_create(weekday=wd)

class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0002_auto_add_subjects"),
    ]

    operations = [
        migrations.RunPython(create_days),
    ]
