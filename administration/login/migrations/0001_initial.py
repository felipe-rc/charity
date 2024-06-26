# Generated by Django 5.0.6 on 2024-05-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                (
                    "role",
                    models.TextField(
                        choices=[
                            ("adm", "Administrador"),
                            ("don", "Doador"),
                            ("aux", "Auxiliado"),
                        ]
                    ),
                ),
            ],
        ),
    ]
