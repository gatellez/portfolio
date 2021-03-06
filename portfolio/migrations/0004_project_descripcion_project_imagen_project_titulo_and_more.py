# Generated by Django 4.0.5 on 2022-06-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_project_descripcion_remove_project_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='descripcion',
            field=models.CharField(default='Descripcion', max_length=250),
        ),
        migrations.AddField(
            model_name='project',
            name='imagen',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='titulo',
            field=models.CharField(default='Titulo', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
