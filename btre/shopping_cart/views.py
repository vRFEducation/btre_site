from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shopping_cart/index.html', {'name' : "Vahid"})


def view(request):
    context = {
        'name' : "Sarah"
    }
    return render(request, "shopping_cart/view.html", context)