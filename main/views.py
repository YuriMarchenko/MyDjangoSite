from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def prices(request):
    return render(request, 'prices.html')


def registrations(request):
    return render(request, 'registrations.html')


def guarantee(request):
    return render(request, 'guarantee.html')


def orders(request):
    return render(request, 'orders.html')


def actions(request):
    return render(request, 'actions.html')


def payments(request):
    return render(request, 'payments.html')
