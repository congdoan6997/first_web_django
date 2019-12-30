from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'
