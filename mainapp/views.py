from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def test_context(requests):
    context = {
        'title': 'test context',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products' : [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ]
    }
    return render(requests, 'mainapp/test-context.html', context)