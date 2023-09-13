from django.shortcuts import render

from catalog.models import Product


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)

    beer_list = Product.objects.all()

    context = {
        'object_list': beer_list
    }

    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)

    return render(request, 'catalog/contact.html')


def product(request, pk):
    info = Product.objects.get(pk=pk)

    context = {
        'object_list': Product.objects.get(pk=pk),
        'name': f'{info.about}',
    }
    return render(request, 'catalog/product.html', context)