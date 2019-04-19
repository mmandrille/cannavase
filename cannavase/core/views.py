from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'construccion.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})