from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Service,Portfolio,Contact

def home(request):
    services = Service.objects.all()[:3]
    portfolios = Portfolio.objects.all()[:6]

    return render(request, 'main/home.html', {'services': services, 'portfolio': portfolios})

def services(request):
    services = Service.objects.all()

    return render(request, 'main/services.html', {'services' : services})


def portfolios(request):
    portfolios = Portfolio.objects.all()

    return render(request, 'main/portfolios.html', {'portfolios' : portfolios})

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
        )
        messages.success(request, 'Thank You! We will return to you as soon as possible')
        return redirect('contact')

    return render(request, 'main/contact.html')