from asyncio.windows_events import NULL
from email.mime import image
from email.policy import default
from turtle import title
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields import URLField

class Project(models.Model):
    titulo = CharField(max_length=100, default="Titulo")
    descripcion = CharField(max_length=250, default="Descripcion")
    imagen = ImageField(default=NULL)
    url=URLField(blank=True)
