from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Product.models import Product

@login_required
def homePage_view(request):
    data = Product.objects.all()

    context = {
        'products': data[:3]
    }

    return render(request, "index.html", context)

@login_required
def aboutUs_view(request):
    return render(request, "aboutUs.html")

def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")
