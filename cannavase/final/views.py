from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# Create your views here.
def cooperamos(request):
    return render(request, 'cooperamos.html', {})

# Create your views here.
def hacemos(request):
    return render(request, 'hacemos.html', {})

# Create your views here.
def somos(request):
    return render(request, 'somos.html', {})