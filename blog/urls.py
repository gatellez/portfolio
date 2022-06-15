from django.urls import path
from .views import render_post


urlpatterns = [
    path('',render_post, name='posts'),
]

