from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def product(request):
      return render(request, 'mainapp/products.html')


