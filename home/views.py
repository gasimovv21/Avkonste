from django.shortcuts import get_object_or_404, render, redirect

from .models import HomeSlideshow, HomeServiceOne, HomeServiceTwo, HomeServiceThird  



def index(request):
    if request.method == "POST":
        if 'services_btn' in request.POST:
            return redirect("services")
        elif 'about_btn' in request.POST:
            return redirect("about")
        elif 'catalog_btn' in request.POST:
            return redirect("catalog")
        elif 'contact_btn' in request.POST:
            return redirect("contact")

    images = HomeSlideshow.objects.all()

    home_service_one = HomeServiceOne.objects.first()
    image_url_one = home_service_one.image.url
    title_one = home_service_one.title
    text_one = home_service_one.text

    home_service_two = HomeServiceTwo.objects.first()
    image_url_two = home_service_two.image.url
    title_two = home_service_two.title
    text_two = home_service_two.text

    home_service_third = HomeServiceThird.objects.first()
    image_url_third = home_service_third.image.url
    title_third = home_service_third.title
    text_third = home_service_third.text

    context = {
        'images' : images,
        'image_url_one': image_url_one,
        'title_one': title_one,
        'text_one': text_one,
        'image_url_two': image_url_two,
        'title_two': title_two,
        'text_two': text_two,
        'image_url_third': image_url_third,
        'title_third': title_third,
        'text_third': text_third,

    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, "contact.html")
