from django.shortcuts import render

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler403(request, exception):
    return render(request, '403.html', status=403)
    
def handler505(request, exception):
    return render(request, '505.html', status=505)