from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def index(request):

    return render(request, 'mainapp/index.html')


def products(request, category_id=None ):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context = {
            'products': products,
            'categories': ProductCategory.objects.all(),
        }
    else:
        context = {
            'products': Product.objects.all(),
            'categories': ProductCategory.objects.all(),
        }
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
