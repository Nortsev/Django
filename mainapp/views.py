from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop'
       }
    return render(request, 'mainapp/index.html', context)


def product(request):
    context = {
        'title': 'GeekShop - Каталог'
    }
    return render(request, 'mainapp/products.html', context)


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
