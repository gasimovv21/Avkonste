from django.shortcuts import render
from .models import Services

def services_view(request):
    services_count = Services.objects.all().count()
    services = Services.objects.all()
    reverse_flag = ""
    i = 0
    for i in range(0, services_count):
        if i % 2 != 0: 
            reverse_flag = "reverseforservices"
        else:
            reverse_flag = ""

    context = {
        'services': services,
        'services_count': services_count,
        'reverse_flag': reverse_flag,
    }
    return render(request, 'services.html', context)