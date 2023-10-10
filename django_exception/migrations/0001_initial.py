# Generated by Django 4.1.9 on 2023-10-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExceptionModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("module", models.CharField(max_length=255)),
                ("filename", models.CharField(max_length=255)),
                ("lineno", models.IntegerField()),
                ("exc_class", models.CharField(max_length=255, verbose_name="Class")),
                (
                    "exc_message",
                    models.CharField(max_length=255, verbose_name="Message"),
                ),
                ("exc_traceback", models.TextField(verbose_name="Traceback")),
                ("timestamp", models.FloatField()),
            ],
            options={
                "verbose_name": "Exception",
                "verbose_name_plural": "Exceptions",
                "db_table": "django_exception",
                "ordering": ("-timestamp",),
                "unique_together": {("filename", "lineno")},
            },
        ),
    ]