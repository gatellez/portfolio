from django.shortcuts import render

def render_post(request):
    return render(request, 'posts.html')
