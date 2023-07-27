from django.shortcuts import render, get_object_or_404

from services.models import Services, SubService, SubServiceDetail

from django.http import JsonResponse

def get_tags_and_subservices(request):
    tag = request.GET.get('tag', None)
    if tag:
        sub_services = SubService.objects.filter(service__tag=tag)
    else:
        sub_services = SubService.objects.all()
    tags = Services.objects.all().values_list('tag', flat=True).distinct()
    services = Services.objects.all()
    context = {
        'tags': tags,
        'sub_services': sub_services,
        'services': services,
    }
    return render(request, 'catalog.html', context)



def sub_services_detail(request, pk):
    sub_service = get_object_or_404(SubService, pk=pk)
    sub_service_details = sub_service.details.all()
    try:
        sub_service_detail = SubServiceDetail.objects.get(sub_service=sub_service)

        images = []
        for detail in sub_service_details:
            images.extend(detail.images.all())

        context = {
            'sub_service_detail': sub_service_detail,
            'sub_service': sub_service,
            'sub_service_details': sub_service_details,
            'images': images,
        }
    except SubServiceDetail.DoesNotExist:
        context = {
            'error_message': 'Bu alt xidmət üçün ətraflı səhifə hələ mövcud deyil..',
        }
    return render(request, 'catalog-detail.html', context)


def get_subservices(request, services_id):
    services = Services.objects.get(id=services_id)
    sub_services = services.subservices.all()
    data = []
    for sub_service in sub_services:
        data.append({
            'sub_servicesId': sub_service.pk,
            'image': sub_service.image.url,
            'title': sub_service.title,
            'text': sub_service.text
        })
    return JsonResponse(data, safe=False)


def get_all_subservices(request):
    sub_services = SubService.objects.all()
    data = []
    for sub_service in sub_services:
        data.append({
            'sub_servicesId': sub_service.pk,
            'image': sub_service.image.url,
            'title': sub_service.title,
            'text': sub_service.text
        })
    return JsonResponse(data, safe=False)