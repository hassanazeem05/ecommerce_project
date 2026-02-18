from django.shortcuts import render
from shop.models import Category

def landing(request):
    return render(request, 'core/landing.html')


def home(request):
    categories = Category.objects.all()
    return render(request, 'core/home.html', {'categories': categories})
