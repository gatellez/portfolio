# Generated by Django 4.0.5 on 2022-06-14 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_description_project_descripcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Descripcion',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Imagen',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Titulo',
        ),
    ]