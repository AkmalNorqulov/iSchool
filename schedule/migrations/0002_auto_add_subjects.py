from django.db import migrations

def add_subjects(apps, schema_editor):
    Subject = apps.get_model("schedule", "Subject")
    subjects = [
        "Adabiyot", "Algebra", "Biologiya", "Fizika", "Geografiya",
        "Geometriya", "Huquq", "Inf va IKT", "Ingliz tili",
        "Jaxon tarixi", "Jismoniy madaniyat", "Kelajak soati",
        "Kimyo", "Ona tili", "Tarbiya", "Texnologiya",
        "O‘zbek tarixi", "O‘zbek tili", "Chizmachilik",
    ]
    for s in subjects:
        Subject.objects.get_or_create(name=s)

class Migration(migrations.Migration):
    dependencies = [("schedule", "0001_initial")]
    operations = [migrations.RunPython(add_subjects)]
