from django.shortcuts import render

def landing_page(request):
    # This looks inside your templates/ folder for landing/index.html
    return render(request, 'landing/index.html')


def Service(request):
    return render(request,'landing/service.html')