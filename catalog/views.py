from django.shortcuts import render

from services.models import Services, SubService


def get_tags_and_subservices(request):
    tag = request.GET.get('tag', None)
    if tag:
        sub_services = SubService.objects.filter(service__tag=tag)
    else:
        sub_services = SubService.objects.all()
    tags = Services.objects.all().values_list('tag', flat=True).distinct()
    context = {
        'tags': tags,
        'sub_services': sub_services,
    }
    return render(request, 'catalog.html', context)

