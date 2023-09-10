from django.shortcuts import render

from catalog.models import Product

# Create your views here.
def homepage(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name} ({email}): {message}')
    return render(request, 'catalog/contacts.html', context)

def index(request):
    return render(request, 'catalog/index.html')