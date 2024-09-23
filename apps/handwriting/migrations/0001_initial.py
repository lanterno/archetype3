# Generated by Django 5.1 on 2024-09-17 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("manuscripts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=10)),
                (
                    "form",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Majuscule", "Majuscule"),
                            ("Minuscule", "Minuscule"),
                            ("Numeral", "Numeral"),
                            ("Punctuation", "Punctuation"),
                            ("Symbol", "Symbol"),
                        ],
                        max_length=11,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feature",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Allograph",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=10)),
                (
                    "character",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="handwriting.character"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Component",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("features", models.ManyToManyField(to="handwriting.feature")),
            ],
        ),
        migrations.CreateModel(
            name="Graph",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("location", models.JSONField()),
                (
                    "allograph",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="handwriting.allograph"),
                ),
                (
                    "item_image",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="manuscripts.itemimage"),
                ),
            ],
        ),
    ]