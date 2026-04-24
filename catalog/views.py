from gc import get_objects

from django.shortcuts import render, get_object_or_404
from catalog.models import Product

def catalog_list(request):
    catalog = Product.objects.all()
    context = {"catalogs": catalog}
    return render(request, 'catalog_list.html', context)


def catalog_detail(request, pk):
    catalogs = get_object_or_404(Product, pk=pk)
    context = {"catalog": catalogs}
    return render(request, 'catalog_detail.html', context)
