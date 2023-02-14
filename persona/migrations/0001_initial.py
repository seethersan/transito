# Generated by Django 4.1.6 on 2023-02-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "email",
                    models.EmailField(max_length=50, primary_key=True, serialize=False),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
            ],
        ),
    ]
