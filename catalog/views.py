from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView

class ProductListView(ListView):
    model = Product
    template_name = 'catalog_list.html'
    context_object_name = 'catalogs'

# def catalog_list(request):
#     catalog = Product.objects.all()
#     context = {"catalogs": catalog}
#     return render(request, 'catalog_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog_detail.html'
    context_object_name = 'catalog'


# def catalog_detail(request, pk):
#     catalogs = get_object_or_404(Product, pk=pk)
#     context = {"catalog": catalogs}
#     return render(request, 'catalog_detail.html', context)
