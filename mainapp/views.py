from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'mainapp/index.html')


def products(request,category_id=None, page =1 ):
    context = {
            'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
    else:
        products = Product.objects.all().order_by('price')
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})

    return render(request, 'mainapp/products.html', context=context)


def test_context(request):
    context = {
        'title': 'добро поЖаловать',
        'username': 'Viktor Dobkin',
        'products': [
            {'name': 'Черное худи', 'price': '2 9990 рублей'},
            {'name': 'Джинсы', 'price': '5 800 рублей'},
        ],
        'promotion': True,
        'promotion_products': [
            {'name': 'Туфли ', 'price': '9 800 рублей'},
        ]
    }

    products = context['products']

    return render(request, 'mainapp/context.html', context)
