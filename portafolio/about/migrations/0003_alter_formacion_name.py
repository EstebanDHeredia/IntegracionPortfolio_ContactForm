# Generated by Django 4.2.11 on 2024-04-19 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_rename_title_formacion_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formacion",
            name="name",
            field=models.CharField(max_length=150, verbose_name="Nombre"),
        ),
    ]