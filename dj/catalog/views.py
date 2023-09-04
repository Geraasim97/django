from django.shortcuts import render




def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)

    return render(request, 'catalog/index.html')


def index1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)

    return render(request, 'catalog/index1.html')
