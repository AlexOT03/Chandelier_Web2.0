# Generated by Django 4.1.9 on 2023-06-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=40)),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=8, max_digits=8)),
                ("duration", models.TimeField(blank=True)),
            ],
        ),
    ]
