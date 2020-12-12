from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop'
       }
    return render(request, 'mainapp/index.html', context)


def product(request):
    context = {'title': 'GeekShop - Каталог',
    'style_link': 'css/products.css',
    'products': [
        {
            'link': 'vendor/img/products/Adidas-hoodie.png',
            'name': 'Худи черного цвета с монограммами adidas Originals',
            'price': '6 090,00 руб.',
            'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
        },
        {
            'link': 'vendor/img/products/Blue-jacket-The-North-Face.png',
            'name': 'Синяя куртка The North Face',
            'price': '23 725,00 руб.',
            'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
        },
        {
            'link': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
            'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
            'price': '3 390,00 руб.',
            'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
        },
        {
            'link': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
            'name': 'Черный рюкзак Nike Heritage',
            'price': '2 340,00 руб.',
            'description': 'Плотная ткань. Легкий материал.'
        },
        {
            'link': 'vendor/img/products/Black-Dr-Martens-shoes.png',
            'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
            'price': '13 590,00 руб.',
            'description': 'Гладкий кожаный верх. Натуральный материал.'
        },
        {
            'link': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
            'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
            'price': '2 890,00 руб.',
            'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
        }

    ]
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
