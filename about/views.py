from django.shortcuts import render
from .models import AboutImages

def about_view(request):
    images = AboutImages.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'about.html', context)
